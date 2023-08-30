import requests
import json
import time
import csv

def get_vacancy(text, page=0):
    params = {
        'text': text, 
    } 
    try:
        req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = req.content.decode()
        out = json.loads(data)['items']
        fields = ["id", "name", "responsibility", "salary", "address", "employment", "employer", "professional_roles", "alternate_url"]
        print(json.dumps(out[page], indent=4))
        address = out[page].get("address")
        # todo написать условие проверяюшее наличие данных в поле
        vacancy = {
            "id": out[page]["id"],
            "name": out[page]["name"],
            "responsibility": out[page]["snippet"]["responsibility"],
            "salary": out[page]["salary"]["from"],
            "address": out[page].get("address"),
            "employment": out[page]["employment"]["name"],
            "employer": out[page]["employer"]["name"],
            "professional_roles": out[page]["professional_roles"][0]["name"],
        }
    except Exception as e:
        print(e)
    # print(out)
    return vacancy

print(get_vacancy("Стажер"))
# get_vacancy("Сварщик")
