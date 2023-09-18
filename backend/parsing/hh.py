import requests
import re


def clean_name(text):
    cleaned_text = re.sub(r'[(.-~),]', '', text)
    return cleaned_text.lower()


def stop_invalid_vacancies(vacancy):
    stop_words = ['senior', 
                  'middle', 
                  'expert', 
                  'techlead', 
                  'tech lead', 
                  'teamlead', 
                  'team lead', 
                  'старший'
                  ]
    for checked_word in clean_name(vacancy.get("name")).split():
        if checked_word in main_words:
            break
        if checked_word in stop_words:
            return True
    return False
  

def get_data_from_vacancy(id):
    server_resp = requests.get(f'https://api.hh.ru/vacancies/{id}')
    if server_resp.status_code != 200:
        return None
    vacancy_data = server_resp.json()
    server_resp.close()
    return vacancy_data


def fetch_hh_vacancies(all_ides, text):
    vacancies, pages = fetch_hh_page_vacancies(all_ides, text)
    for page in range(1, pages):
        page_vacancies, _ = fetch_hh_page_vacancies(all_ides, text, page)
        vacancies.extend(page_vacancies)
    return vacancies


def get_salary(txt_dict):
    if not txt_dict["currency"]:
        return None 
    salary_from = txt_dict["from"] if txt_dict.get("from") else ''
    salary_to = txt_dict["to"] if txt_dict.get("to") else ''
    if salary_from and salary_to:
        salary = str(salary_from) + ' - ' + str(salary_to) + ' ' + txt_dict["currency"]
    elif salary_from and not salary_to:
        salary = str(salary_from) + ' ' + txt_dict["currency"]
    elif not salary_from and salary_to:
        salary = str(salary_to) + ' ' + txt_dict["currency"]
    return salary


def get_internship(text):
    pattern = r'\b(?:стажировка|internship)\b'
    matches = re.findall(pattern, text, re.IGNORECASE)
    return True if matches else False


def fetch_hh_page_vacancies(all_ides, text, page=0):
    params = {
        'text': text,
        'search_field': ['name'],
        'per_page': 20,
        'page': page
    }
    response = requests.get('https://api.hh.ru/vacancies', params)
    data = response.json()
    response.close()
    pages = data['pages']
    items = data['items']
    vacancies = []
    for item in items:
        vacancy_data = get_data_from_vacancy(item.get("id"))
        if stop_invalid_vacancies(item):
            break    
        vacancy = {
            "id": item.get("id"),
            "company_name": item.get("employer")["name"] if item.get("employer") else None,
            "title": item.get("name"),
            "salary": get_salary(vacancy_data["salary"]) if vacancy_data and vacancy_data["salary"] else None,
            "location": item.get("address")["raw"] if item.get("address") else None,
            "speciality": text.split(' ')[1],
            "internship": get_internship(item.get("employment")["name"] if item.get("employment") else None),
            "remote": True if item.get("schedule") and item.get("schedule")["name"] == 'удаленная работа' else False,
            "url": vacancy_data["alternate_url"] if vacancy_data and vacancy_data["alternate_url"] else None,
            "description": vacancy_data["description"] if vacancy_data and vacancy_data["description"] else None,
        }
        if vacancy["id"] not in all_ides:
            vacancies.append(vacancy)
            all_ides.add(vacancy["id"])
        if vacancy['description'] and re.search(r"удаленная работа|удаленн", vacancy['description'], re.IGNORECASE):
            vacancy["remote"] = True   
        if vacancy['description'] and re.search(r'\bне удаленная\b|\bудаленная не\b', vacancy['description'], re.IGNORECASE):
            vacancy["remote"] = False 
    return vacancies, pages


def get_vacancies(main_words, languages_stacks):
    all_ides = set()
    result = []
    for word in main_words:
        for stack in languages_stacks:
            vacancies = fetch_hh_vacancies(all_ides, f"{word} {stack}")
            result.extend(vacancies)
    return result


from database import get_db
from crud import create_vacancy
def import_vacancies():
    result = get_vacancies(main_words, languages_stacks)
    for db in get_db():
        for job in result:
            create_vacancy(db, job)

import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def clear_db():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )

        cur = conn.cursor()

        cur.execute("DELETE FROM vacancies;")

        conn.commit()

        cur.close()
        conn.close()
    except Exception as e:
        print("Error: ", str(e))


main_words = ['junior', 
              'intern', 
              'стажер', 
              'младший', 
              'начинающий',
                ]
languages_stacks = ['python', 
                    'java', 
                    'javascript', 
                    'data science', 
                    'qa', 
                    'c#',
                    'frontend', 
                    'backend', 
                    ]


if __name__ == "__main__":
    clear_db()
    import_vacancies()
