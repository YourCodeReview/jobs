import requests
import json
import time
import csv

def get_vacancy(text):
    params = {
        'text': text, 
    } 
    req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
    data = req.content.decode()
    out = json.loads(data)['items']
    fields = ["id", "name", "description", "salary", "address", "employment", "employer", "professional_roles", "alternate_url"]
    vacancy = {
        "id": out["id"],
        "name": out["name"],
        "description": out["description"],
        "salary": out["salary"]
    }
    return vacancy

get_vacancy("Сварщик")
