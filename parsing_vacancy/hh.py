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


def fetch_hh_vacancies(all_ides, text):
    """ Собирает все вакансии с hh по ключевым словам """
    vacancies, pages = fetch_hh_page_vacancies(all_ides, text)
    for page in range(1, pages):
        page_vacancies, _ = fetch_hh_page_vacancies(all_ides, text, page)
        vacancies.extend(page_vacancies)
    return vacancies


def fetch_hh_page_vacancies(all_ides, text, page=0):
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
            "schedule": item.get("schedule")["name"] if item.get("schedule") else None,
        }
        if vacancy["hh_id"] not in all_ides:
            vacancies.append(vacancy)
            all_ides.add(vacancy["hh_id"])
    return vacancies, pages

if __name__ == "__main__":
    start = time.time()
    main_words = ['junior', 
                  'intern', 'стажер', 'младшый',
                  ]
    languages_stacks = ['php', 
                        'java', 'javascript', 'data science', 'python',
                        'qa', 'c++', 'c#', 'c', 'sql', 'postgresql', 'vue.js',
                        'frontend', 'backend', 'ml', 'ds', 'mysql', 'js',
                        'flask', 'django', 'fastapi', 'data ingeneer', 'ruby on rails',
                        'react.js', 'angular.js', 'node.js', 'swift', 'kotlin', 'unity',
                        'ruby', 'go', 'rust', 'html/css', 'mongodb', 'nosql', 'devops', 'docker',
                        ]
    result = []
    all_ides = set()
    for word in main_words:
        temp_list = []
        for stack in languages_stacks:
            vacancies = fetch_hh_vacancies(all_ides, f"{word} {stack}")
            result.extend(vacancies)
    with open('result.json', 'w', encoding='utf-8', errors='ignore') as f:
        f.write(json.dumps(result, indent=4, ensure_ascii=False))
    end = time.time()
    print('вакансии:', len(result))
    print('время ожидания:', round((end - start) / 60), 'мин.')
    print(time.asctime())

