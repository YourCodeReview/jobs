import requests
import json


def get_description_from_vacancy(id):
    """ Возвращает полное описание вакансии по id """
    vacancy_data = requests.get(f'https://api.hh.ru/vacancies/{id}').json()
    return vacancy_data['description']


def fetch_hh_vacancies(text):
    """ Собирает все вакансии с hh по ключевым словам """
    vacancies, pages = fetch_hh_page_vacancies(text)
    for page in range(1, pages):
        page_vacancies, _ = fetch_hh_page_vacancies(text, page)
        vacancies.extend(page_vacancies)
    return vacancies


def fetch_hh_page_vacancies(text, page=0):
    """ Собирает все вакансии с одной страницы hh по ключевым словам """
    params = {  # параметры обращения к api
        'text': text,
        'search_field': ['name'],
        'per_page': 20,
        'page': page  # номер страницы
    }
    response = requests.get('https://api.hh.ru/vacancies', params)
    data = response.json()

    pages = data['pages']
    items = data['items']
    vacancies = []

    for item in items:
        vacancy = {
            "hh_id": item.get("id"),
            "name": item.get("name"),
            "requirement": item.get("snippet")["requirement"],
            "responsibility": item.get("snippet")["responsibility"],
            "description": get_description_from_vacancy(item.get("id")),
            "salary": item.get("salary"),
            "address": item.get("address")["raw"] if item.get("address") else None,
            "employment": item.get("employment")["name"],
            "professional_roles": item.get("professional_roles")[0]["name"],
        }
        vacancies.append(vacancy)

    return vacancies, pages


result = fetch_hh_vacancies("junior java")

print(json.dumps(result, indent=4, ensure_ascii=False))
print(len(result))
