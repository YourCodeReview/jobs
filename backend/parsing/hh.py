import requests


def clean_name(text):
    return text.replace('(', '').replace(')', '').replace(',', '').lower()


def stop_invalid_vacancies(vacancy):
    stop_words = ['senior', 
                  'middle', 
                  'expert', 
                  'techlead', 
                  'tech lead', 
                  'teamlead', 
                  'team lead', 
                  'старший']
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
            "hh_id": item.get("id"),
            "name": item.get("name"),
            'area': item.get("area")["name"] if item.get("area") else None,
            "description": vacancy_data["description"] if vacancy_data and vacancy_data["description"] else None,
            "address": item.get("address")["raw"] if item.get("address") else None,
            "employment": item.get("employment")["name"] if item.get("employment") else None,
            "employer": item.get("employer")["name"] if item.get("employer") else None,
            "schedule": vacancy_data["schedule"]["name"] if vacancy_data and vacancy_data["schedule"] else None,
            "url": vacancy_data["alternate_url"] if vacancy_data and vacancy_data["alternate_url"] else None,
            "salary": vacancy_data["salary"] if vacancy_data and vacancy_data["salary"] else None,
            "specialty": text.split(' ')[1],
        }
        if vacancy["hh_id"] not in all_ides:
            vacancies.append(vacancy)
            all_ides.add(vacancy["hh_id"])
    return vacancies, pages


if __name__ == "__main__":
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
    result = []
    all_ides = set()
    for word in main_words:
        temp_list = []
        for stack in languages_stacks:
            vacancies = fetch_hh_vacancies(all_ides, f"{word} {stack}")
            result.extend(vacancies)