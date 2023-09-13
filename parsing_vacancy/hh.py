import requests
import json
import time


def stop_invalid_vacancies(vacancy):
    ''' Проверяет на валидность вакансии '''
    stop_words = ['senior', 'middle', 'expert', 'techlead', 'tech lead', 
                  'teamlead', 'team lead', 'старший']
    for checked_word in vacancy.get("name").replace('(', '').replace(')', '').replace(',', '').lower().split():
        if checked_word in main_words:
            break
        if checked_word in stop_words:
            return True
    return False
  

def get_data_from_vacancy(id):
    """ Возвращает полное описание вакансии по id """
    server_resp = requests.get(f'https://api.hh.ru/vacancies/{id}')
    if server_resp.status_code != 200:
        return None
    vacancy_data = server_resp.json()
    server_resp.close()
    return vacancy_data


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
        vacancy_data = get_data_from_vacancy(item.get("id"))

        if stop_invalid_vacancies(item):
            # создает файл на локальный диск
            with open('log.txt', 'w', encoding='utf-8', errors='ignore') as f:
                f.write(f"id: {item['id']}, {item['name']}\n")
            
            # создает файл на сервере
            # with open('/root/jobs/backend/parsing/log.txt', 'a', encoding='utf-8', errors='ignore') as f:
            #     f.write(f"id: {item['id']}, {item['name']}\n")
            
            break    

        vacancy = {
            "hh_id": item.get("id"),
            "name": item.get("name"),
            'area': item.get("area")["name"] if item.get("area") else None,
            # "requirement": item.get("snippet")["requirement"] if item.get("snippet") else None,
            # "responsibility": item.get("snippet")["responsibility"] if item.get("snippet") else None,
            "description": vacancy_data["description"] if vacancy_data and vacancy_data["description"] else None,
            # "salary_from": item.get("salary")["from"] if item.get("salary") else None,
            # "salary_to": item.get("salary")["to"] if item.get("salary") else None,
            # "salary_currency": item.get("salary")["currency"] if item.get("salary") else None,
            "address": item.get("address")["raw"] if item.get("address") else None,
            "employment": item.get("employment")["name"] if item.get("employment") else None,
            "employer": item.get("employer")["name"] if item.get("employer") else None,
            # "professional_roles": item.get("professional_roles")[0]["name"] if item.get("professional_roles")[0] else None,
            "schedule": vacancy_data["schedule"]["name"] if vacancy_data and vacancy_data["schedule"] else None,
            # "vacancy_data": vacancy_data,
            "url": vacancy_data["alternate_url"] if vacancy_data and vacancy_data["alternate_url"] else None,
            "salary": vacancy_data["salary"] if vacancy_data and vacancy_data["salary"] else None,
            "specialty": text.split(' ')[1],
        }

        if vacancy["hh_id"] not in all_ides:
            vacancies.append(vacancy)
            all_ides.add(vacancy["hh_id"])

    return vacancies, pages

if __name__ == "__main__":
    start = time.time()
    main_words = ['junior', 
                #   'intern', 'стажер', 'младший', 'начинающий'
                  ]
    languages_stacks = [
                        # 'python', 
                        'java', 
                        # 'javascript', 'data science', 'qa', 'c#',
                        # 'frontend', 'backend', 
                        # 'r', 'pandas', 'php',
                        # 'c++', 'c', 'sql', 'postgresql', 'vue.js',
                        # 'ml', 'ds', 'mysql', 'js', "greenplum",
                        # 'flask', 'django', 'fastapi', 'data ingeneer', 'ruby',
                        # 'react', 'angular', 'node', 'swift', 'kotlin', 'unity',
                        # 'ruby', 'go', 'rust', 'html/css', 'mongodb', 'nosql', 'devops', 'docker',
                        ]
    result = []
    all_ides = set()
    for word in main_words:
        temp_list = []
        for stack in languages_stacks:
            vacancies = fetch_hh_vacancies(all_ides, f"{word} {stack}")
            result.extend(vacancies)

    # создает файл на локальный диск
    with open('result.json', 'w', encoding='utf-8', errors='ignore') as f:
        f.write(json.dumps(result, indent=4, ensure_ascii=False))

    # создает файл на сервере
    # with open('/root/jobs/backend/parsing/result.json', 'w', encoding='utf-8', errors='ignore') as f:
    #     f.write(json.dumps(result, indent=4, ensure_ascii=False))
    
    end = time.time()
    print('вакансии:', len(result))
    print('время ожидания:', round((end - start) / 60), 'мин.')
    print(time.asctime())