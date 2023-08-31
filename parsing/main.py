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
        
        vacancy = {}

        if not out[page]["id"]:
            vacancy["id"] = 'null'
        else:
            vacancy["id"] = out[page]["id"]
        
        if not out[page]["name"]:
            vacancy["name"] = 'null'
        else:
            vacancy["name"] = out[page]["name"]
        
        if not out[page]["snippet"]["responsibility"]:
            vacancy["responsibility"] = 'null'
        else:
            vacancy["responsibility"] = out[page]["snippet"]["responsibility"]

        if not out[page]["salary"]:
            vacancy["salary"] = 'null'
        else:
            vacancy["salary"] = out[page]["salary"]["from"]

        if not out[page]["address"]:
            vacancy["address"] = 'null'
        else:
            vacancy["address"] = out[page]["address"]["name"]

        if not out[page]["employment"]:
            vacancy["employment"] = 'null'
        else:
            vacancy["employment"] = out[page]["employment"]["name"]
        
        if not out[page]["employer"]:
            vacancy["employer"] = 'null'
        else:
            vacancy["employer"] = out[page]["employer"]["name"]

        if not out[page]["professional_roles"]:
            vacancy["professional_roles"] = 'null'
        else:
            vacancy["professional_roles"] = out[page]["professional_roles"][0]["name"]


        # vacancy = {
        #     "id": out[page]["id"],
        #     "name": out[page]["name"],
        #     "responsibility": out[page]["snippet"]["responsibility"],
        #     "salary": out[page]["salary"]["from"],
        #     "address": out[page].get("address"),
        #     "employment": out[page]["employment"]["name"],
        #     "employer": out[page]["employer"]["name"],
        #     "professional_roles": out[page]["professional_roles"][0]["name"],
        # }
    except Exception as e:
        print(e)
    return vacancy

print(json.dumps(get_vacancy("стажер C++"), indent=4, ensure_ascii=False))
# get_vacancy("стажер C++")