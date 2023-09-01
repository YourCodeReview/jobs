import requests
import json
import time
import csv

def get_description_from_vacancy(id):
    """
    возвращает описание вакансии.
    """
    response = json.loads(requests.get(f'https://api.hh.ru/vacancies/{id}').content.decode())['description']
    return response

def get_all_vacancies(text):
    """
    собирает все вакансии и получает количество страниц page_vacansies
    возвращает все вакансии 
    """

    vacansies, pages = get_vacancies(text)
    for page in range(1, pages):

        page_vacansies, _ = get_vacancies(text, page)

        vacansies.extend(page_vacansies)
    return vacansies

def get_vacancies(text, page=0):
    """
    возвращает объявления на конкретной страниуе
    """

    params = { # параметры обращения к api
        'text': text,  # искомая вакансия
        'per_page': 20, # кол. вакансий на страницу
        'page': page  # номер страницы
    } 

    # ответ api 
    response = requests.get('https://api.hh.ru/vacancies', params)  

    # декодированные данные (строка)
    data = response.content.decode()

    # данные в формате json
    response_data = json.loads(data)

    # общая количество страниц
    pages = response_data['pages']

    # вакансии на текущей странице
    items = response_data['items']
 
    # fields = ["id", "name", "responsibility", "salary", "address", "employment", "employer", "professional_roles", "alternate_url"]
   
    vacansies = []

    for item in items:
        vacancy = {}

# -- id ----------------------------------------
        if not item["id"]:
            vacancy["id"] = 'null'
        else:
            vacancy["id"] = item["id"]

# -- name ----------------------------------------
        if not item["name"]:
            vacancy["name"] = 'null'
        else:
            vacancy["name"] = item["name"]

# -- requirement ----------------------------------------
        if not item["snippet"]["requirement"]:
            vacancy["requirement"] = 'null'
        else:
            vacancy["requirement"] = item["snippet"]["requirement"]

# -- responsibility ----------------------------------------
        if not item["snippet"]["responsibility"]:
            vacancy["responsibility"] = 'null'
        else:
            vacancy["responsibility"] = item["snippet"]["responsibility"]
        # time.sleep(0.25)
# -- description ----------------------------------------
        if not get_description_from_vacancy(f'{vacancy["id"]}'):
            vacancy["description"] = 'null'
        else:
            vacancy["description"] = get_description_from_vacancy(f'{vacancy["id"]}')

# -- salary ----------------------------------------
        if not item["salary"]:
            vacancy["salary"] = 'null'
        else:
            vacancy["salary"] = item["salary"]["from"]

# -- address ----------------------------------------
        if not item["address"]:
            vacancy["address"] = 'null'
        else:
            vacancy["address"] = item["address"]["city"]

# -- employment ----------------------------------------
        if not item["employment"]:
            vacancy["employment"] = 'null'
        else:
            vacancy["employment"] = item["employment"]["name"]

# -- employer ----------------------------------------
        if not item["employer"]:
            vacancy["employer"] = 'null'
        else:
            vacancy["employer"] = item["employer"]["name"]

# -- professional_roles ----------------------------------------
        if not item["professional_roles"]:
            vacancy["professional_roles"] = 'null'
        else:
            vacancy["professional_roles"] = item["professional_roles"][0]["name"]
            
# ------------------------------------------
        vacansies.append(vacancy)

    return vacansies, pages

result = get_all_vacancies("сопожник")

print(json.dumps(result, indent=4, ensure_ascii=False))

print(len(result))

# print(get_description_from_vacancy('85117536'))