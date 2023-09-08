import requests
import json
import time


def get_description_from_vacancy(id):
    """ Возвращает полное описание вакансии по id """
    server_resp = requests.get(f'https://api.hh.ru/vacancies/{id}')
    if server_resp.status_code != 200:
        return None
    vacancy_data = server_resp.json()
    server_resp.close()
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
    response.close()
    pages = data['pages']
    items = data['items']
    vacancies = []
    for item in items:
        vacancy = {
            "hh_id": item.get("id"),
            "name": item.get("name"),
            'area': item.get("area")["name"] if item.get("area") else None,
            "requirement": item.get("snippet")["requirement"] if item.get("snippet") else None,
            "responsibility": item.get("snippet")["responsibility"] if item.get("snippet") else None,
            "description": get_description_from_vacancy(item.get("id")),
            "salary_from": item.get("salary")["from"] if item.get("salary") else None,
            "salary_to": item.get("salary")["to"] if item.get("salary") else None,
            "salary_currency": item.get("salary")["currency"] if item.get("salary") else None,
            "address": item.get("address")["raw"] if item.get("address") else None,
            "employment": item.get("employment")["name"] if item.get("employment") else None,
            "employer": item.get("employer")["name"] if item.get("employer") else None,
            "professional_roles": item.get("professional_roles")[0]["name"] if item.get("professional_roles")[0] else None,
        }
        vacancies.append(vacancy)
    return vacancies, pages

if __name__ == "__main__":
    start = time.time()
    main_words = ['junior', 'intern', 'стажер', 'младшый']
    languages_stacks = ['php', 'java', 'javascript', 'data science', 
                        'qa', 'c++', 'c#', 'c', 'sql', 'postgresql',
                        'frontend', 'backend', 'ml', 'ds', 'mysql', 
                        'flask', 'django', 'fastapi', 'data ingeneer']
    result = []
    for word in main_words:
        temp_list = []
        for stack in languages_stacks:
            temp_list.append(fetch_hh_vacancies(f"{word} {stack}"))
            result.extend(temp_list)
    with open('result.json', 'w', encoding='utf-8', errors='ignore') as f:
        f.write(json.dumps(result, indent=4, ensure_ascii=False))
    end = time.time()
    print(len(result), 'time:', round((end - start) / 60), 'мин.', time.asctime)

