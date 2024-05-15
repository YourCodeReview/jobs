import re
import time

import requests
from bs4 import BeautifulSoup


def vacancy_validation(vacancy_title):
    """Функция проверяет заголовок вакансии на наличие слов из списка направлений, по которым мы ведем поиск,
    а также проверяет наличие слов из списка "грэйдов" (stop words), которые мы хотим исключить из поиска.

    Вход: Заголовок вакансии.
    Выход: - True, если присутствует любое слово из списка languages_stacks и отсутствуют слова из списка stop_words.
           - False во всех остальных случаях."""
    languages_stacks = [
        "python",
        "java",
        "javascript",
        "qa",
        "c#",
        "data scientist",
        "data science",
        "data analyst",
        "frontend",
        "backend",
    ]

    stop_words = [
        "senior",
        "(senior)",
        "middle",
        "(middle)",
        "expert",
        "techlead",
        "tech lead",
        "teamlead",
        "team lead",
        "lead",
        "старший",
        "заместитель",
        "руководитель",
        "ведущий",
    ]

    if any(keyword in vacancy_title.lower() for keyword in languages_stacks):
        if any(stop_word in vacancy_title.lower() for stop_word in stop_words):
            return False
        return True
    else:
        return False


def make_request(url):
    """Функция для обработки ошибки 429. Если при запросе мы получаем такой ответ,
    то эта функция выполняет повторный запрос через 5 секунд.

    Вход: URL, по которому выполняется запрос.
    Выход: - Ответ сервера, если запрос выполнен успешно.
           - Повторный вызов этой функции, если возникла ошибка 429.
           - Наименование другой ошибки, если возникла иная ошибка."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as err:
        if response.status_code == 429:
            print(
                "Слишком много запросов, через 5 секунд будет отправлен повторный зарос"
            )
            time.sleep(5)
            return make_request(url)
        else:
            raise err


def parse_vacancy(vacancy):
    """Основная функция для парсинга вакансий. Она принимает отдельные элементы div, собранные в функции parse_all_page,
    и извлекает из них следующие данные: заголовок, название компании, местоположение вакансии и URL со ссылкой на вакансию.
    Затем функция извлекает refid и tracking_id из ссылки на вакансию и формирует ссылку на описание вакансии.
    После этого она обрабатывает ответ по этой ссылке.
    Все полученные данные сохраняются в словарь vacancy и возвращаются функцией.

    Выход: словарь "vacancy" """
    title = vacancy.find("h3", class_="base-search-card__title").text
    if not vacancy_validation(title):
        return None

    company_name = vacancy.find("h4", class_="base-search-card__subtitle").text
    location = vacancy.find("span", class_="job-search-card__location").text
    url_vacancy = vacancy.find(
        "a",
        class_="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]",
    ).get("href")

    pattern_before_position = r".{10}(?=\?position)"
    pattern_trackingid_position = r"trackingId=([^&]+)&trk"

    match_before_refid = re.search(pattern_before_position, url_vacancy)
    match_trackingid_position = re.search(pattern_trackingid_position, url_vacancy)

    ten_chars_before_refid = match_before_refid.group(0)
    tracking_id = match_trackingid_position.group(1)
    detail_url = f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{ten_chars_before_refid}?trackingId={tracking_id}"

    r_description = make_request(detail_url)
    soup_detail = BeautifulSoup(r_description.text, "lxml")
    div_element = soup_detail.select_one(
        ".show-more-less-html__markup.show-more-less-html__markup--clamp-after-5"
    )

    r_text = []
    for tag in div_element.find_all(["p", "li"]):
        if tag.name == "li":
            r_text.append("• " + tag.get_text())
        else:
            r_text.append(tag.get_text())

    vacancy = {
        "company_name": company_name.strip(),
        "title": title.strip(),
        "location": location.strip(),
        "url": url_vacancy,
        "description": r_text,
    }

    return vacancy


def parse_one_page(all_vacancy_on_page):
    """В данной функции создается список vacancy_list и вызывается цикл for,
    который проходит по каждому отдельному элементу div из списка all_vacancy_on_page.
    Затем для каждого элемента вызывается функция parse_vacancy, и полученные вакансии добавляются в список vacancy_list.

    Вход: переменная all_vacancy_on_page
    Выход: список вакансий с одной страницы vacancy_list"""
    vacancy_list = []
    for vacancy in all_vacancy_on_page:
        parsed_vacancy = parse_vacancy(vacancy)
        if parsed_vacancy is not None:
            vacancy_list.append(parsed_vacancy)
    return vacancy_list


def parse_all_page():
    """Функция для сбора данных со всех страниц с открытым доступом (без авторизации), на которых выводится список вакансий.
    Цикл for проходит по каждому geoid из списка, и для каждого элемента вызывается цикл while.
    В цикле while выполняется запрос на страницу со списком вакансий (каждая страница возвращает по 10 вакансий).
    Полученный ответ обрабатывается с помощью BeautifulSoup, где ищутся интересующие нас элементы,
    и записываются в переменную all_vacancy_on_page.
    Затем вызывается функция parse_one_page и передается переменная all_vacancy_on_page.
    В начале функции создается список vacancy_list.
    По ходу работы функции он дополняется, и в конце возвращается результат парсинга всех доступных страниц.

    Выход: список вакансий со всех страниц vacancy_list
    """
    vacancy_list = []
    list_geoid = [
        101728296,
        101705918,
    ]  # список geoid, они подставляются в ссылку по которой будем делать запрос.
    for geoid in list_geoid:
        start = 0
        while start < 1000:
            url = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=&location=&geoId={geoid}&trk=guest_homepage-basic_jobs-search-bar_search-submit&start={start}"
            print(f"Обрабатывается страница {url}")
            r = make_request(url)
            print(f"Status Code: {r.status_code}")
            print(f"Status Message: {r.reason}")
            soup = BeautifulSoup(r.text, "lxml")
            all_vacancy_on_page = soup.findAll(
                "div",
                class_="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card",
            )
            if all_vacancy_on_page == []:
                print("Следующие страницы не содержат вакансий")
                break
            new_vacancies = parse_one_page(all_vacancy_on_page)
            vacancy_list.extend(new_vacancies)
            start += 10
            time.sleep(1)
    return vacancy_list


list_of_vacancies = parse_all_page()  # Список полученных вакансий
print(f"Итого: количество подходящих вакансий - {len(list_of_vacancies)}")
