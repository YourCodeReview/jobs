import requests


import json
import time
import csv



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
        if not item["id"]:
            vacancy["id"] = 'null'
        else:
            vacancy["id"] = item["id"]

        if not item["name"]:
            vacancy["name"] = 'null'
        else:
            vacancy["name"] = item["name"]

        if not item["snippet"]["requirement"]:
            vacancy["requirement"] = 'null'
        else:
            vacancy["requirement"] = item["snippet"]["requirement"]

        if not item["snippet"]["responsibility"]:
            vacancy["responsibility"] = 'null'
        else:
            vacancy["responsibility"] = item["snippet"]["responsibility"]

        if not item["salary"]:
            vacancy["salary"] = 'null'
        else:
            vacancy["salary"] = item["salary"]["from"]

        if not item["address"]:
            vacancy["address"] = 'null'
        else:
            vacancy["address"] = item["address"]["city"]

        if not item["employment"]:
            vacancy["employment"] = 'null'
        else:
            vacancy["employment"] = item["employment"]["name"]

        if not item["employer"]:
            vacancy["employer"] = 'null'
        else:
            vacancy["employer"] = item["employer"]["name"]

        if not item["professional_roles"]:
            vacancy["professional_roles"] = 'null'
        else:
            vacancy["professional_roles"] = item["professional_roles"][0]["name"]

        vacansies.append(vacancy)

    return vacansies, pages


result = get_all_vacancies("стажер C++")

print(json.dumps(result, indent=4, ensure_ascii=False))

print(len(result))

