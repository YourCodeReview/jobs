import re
import os
import time
from typing import Tuple, Dict, List
from bs4 import BeautifulSoup
import requests

from dotenv import find_dotenv, load_dotenv
from parsing.utils import perform_import
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

# Получение переменных окружения
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
PASSWORD = os.getenv("PASSWORD")
PHONE_NUMBER = os.getenv("PHONE")
SESSION_NAME = "session_name"

# Инициализация TelegramClient
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
client.start(password=PASSWORD, phone=PHONE_NUMBER)


languages_stacks = [
    "python",
    "java",
    "javascript",
    "qa",
    "c#",
    "data scientist",
    "data science",
    "data analyst",
    "data engineer",
    "ml",
    "аналитик данных",
    "frontend",
    "backend",
]


def convert_dict_to_text_format(data_dict: Dict) -> str:
    """
    Функция конвертирует словарь в нужный текстовый формат.

    :param data_dict: Словарь данных.
    :return: Текстовая строка в нужном формате.
    """
    links_info = []
    start_index = 0

    # Итерация по сущностям в словаре.
    for entity in data_dict.get("entities", []):
        # Если сущность - текстовая ссылка
        if entity["_"] == "MessageEntityTextUrl":
            # Вычисление индексов текста ссылки в сообщении.
            end_index = entity.get("offset", 0) + entity.get("length", 0)
            link_text = data_dict["message"][start_index:end_index]
            start_index = end_index
            link_url = entity.get("url", "")
            links_info.append(f"{link_text} {link_url}")

    # Сборка и объединение информации о ссылках в строку.
    return "".join(links_info)


def get_company_name_and_title(data: str) -> Tuple[str, str]:
    """
     Функция получает company_name и title из входных данных.

    :param data: Входные данные, которые предварительно валидируются на соответствие.
    :return: Кортеж, содержащий title и company_name.
    """

    # Разбивка входных данных по символу ' / '
    data_list = data.split(' / ')
    if len(data_list) != 2:
        return data, "Имя компания отсутствует"
    title = data_list[0].strip()
    company_name = data_list[1].strip()
    return title, company_name


def get_vacancies(data: str) -> List[List[str]]:
    """
    Функция для извлечения информации о вакансиях из текста.

    :param data: Входные данные в виде строки, представляющей собой текст с информацией о вакансиях.
    :return: Список списков строк, представляющих информацию о вакансиях.
    """

    # Разделяем входные данные по двойным переносам строки и отбираем только те строки, где есть "подробнее".
    vacancies = [message.split("\n") for message in data.split("\n\n") if "подробнее" in message.lower()]

    return vacancies


def get_location(data: str) -> Tuple[bool, str]:
    """
    Функция получения информации о местоположении (удалённая работа или указанное место).

    :param data: Входные данные с информацией о вакансии.
    :return: Кортеж (удалённая работа - True/False, местоположение).
    """
    # Значения по умолчанию
    location = "Удалённо"
    remote = True

    # Разбиваем текст на две части: местоположение и остаток текста.
    parsing_text = data.lower().split(".", maxsplit=1)

    # Если в первой части не указано "удалённо", то считаем, что это указанное место.
    if "удалённо" not in parsing_text[0]:
        location = parsing_text[0].strip().title()
        remote = False

    return remote, location


def get_urls(data: str) -> List:
    """
    Функция для извлечения всех URL-ссылок из текста.

    :param data: Входные данные с текстом.
    :return: Список URL-ссылок.
    """
    urls = re.findall(r'https?://\S+', data)
    return urls

def get_description(telegram_description: str, url) -> (str, None):
    """
    Функция для извлечения описания.

    :param telegram_description: Входные данные с текстом.
    :param url: Ссылка подробнее
    :return: Описание вакансии.
    """
    if 'https://career.habr.com' in url:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            description = soup.find("div", {"class": "vacancy-description__text"})
            return description.decode_contents()
        return None
    elif 'https://www.vseti.app' in url:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                response.encoding = 'utf8'
                soup = BeautifulSoup(response.text, "html.parser")
                description = soup.find("div", {"class": "rich-text-block w-richtext"})
                return description.decode_contents()
            return None
        except requests.exceptions.SSLError:
            print('Max retries exceeded with url')
            time.sleep(1)
            return f"{telegram_description.strip()}. Подробнее: {url}"

    return f"{telegram_description.strip()}. Подробнее: {url}"

def telegram_get_vacancies_messages():
    target_group_id = -1001626257345   #https://t.me/young_june

    limit = 100
    offset_id = 0
    history = client(GetHistoryRequest(
        peer=PeerChannel(target_group_id),
        offset_id=offset_id,
        offset_date=None,
        add_offset=0,
        limit=limit,
        max_id=0,
        min_id=0,
        hash=0
    ))

    # Проверка наличия сообщений
    if history.messages:
        data_dict = (message.to_dict() for message in history.messages)
        return data_dict
    else:
        print("Получено пустое сообщение истории в Telegram.")
        return []


def telegram_get_vacancy_data(data, vacancy, sequence_number):
    try:
        title, company_name = get_company_name_and_title(vacancy[0])
        for spec_in_title in title.split():
            if spec_in_title.lower() in languages_stacks:
                speciality = spec_in_title.lower()
                break
        else:
            return
        remote, location = get_location(vacancy[1])
        date = data["date"]
        urls = get_urls(vacancy[2])
        if len(urls) == 2:
            url = urls[1]
        else:
            url = urls[0]
        # description = f"{vacancy[1].strip()}. Подробнее: {urls[0]}"
        description = get_description(vacancy[1], urls[0])
        if not description:
            return
        vacancy_data = {
            "id": f"telegram_{data['id'] * 100 + sequence_number}",
            "title": title,
            "company_name": company_name,
            "description": description,
            "url": url,
            "remote": remote,
            "location": location,
            "salary": "Не указана",
            "speciality": speciality,
            "internship": False,
            "date_publication": date,
        }
        return vacancy_data
    except IndexError:
        print(f"Была ошибка: {data}")


def telegram_get_vacancies_info():
    all_vacancies = []
    for telegram_message in telegram_get_vacancies_messages():
        text = convert_dict_to_text_format(telegram_message)
        vacancies = get_vacancies(text)
        for sequence_number, vacancy in enumerate(vacancies):
            valid_vacancy = telegram_get_vacancy_data(telegram_message, vacancy, sequence_number)
            if valid_vacancy:
                all_vacancies.append(valid_vacancy)
    return all_vacancies


if __name__ == "__main__":
    print("Импорт Telegram")
    perform_import(telegram_get_vacancies_info)
