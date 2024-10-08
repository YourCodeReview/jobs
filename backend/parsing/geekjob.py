import datetime
import locale
import re
import requests
import time
from bs4 import BeautifulSoup
from parsing.utils import perform_import


locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")

# param 't' через запятую
geekjobs_specialty = {
    "python": "2,3,308",
    "java": "2,3,301",
    "javascript": "2,3,302",
    "qa": "2,32",
    "c#": "2,3,292",
    "data": "52",
}
# param 't' через запятую (combine specialty + positions)
geekjobs_position = {
    "Intern": "276",
    "Junior": "277",
    "Intern+Junior": "276,277",
}
stop_words = [
    "senior",
    "middle",
    "expert",
    "techlead",
    "tech lead",
    "teamlead",
    "team lead",
    "lead",
    "старший",
    "заместитель",
]


def geekjob_get_vacancies_raw_data() -> list:
    raw_data = []
    base_url = "https://geekjob.ru/json/find/vacancy"
    for specialty, specialty_id in geekjobs_specialty.items():
        params = {
            "page": 1,
            "t": f"{specialty_id},{geekjobs_position['Intern+Junior']}",
        }
        req = requests.get(base_url, params=params)
        data = req.json()["data"]
        for vacancy in data:
            vacancy["speciality"] = specialty
        time.sleep(0.5)
        raw_data.extend(data)

    return raw_data


def geekjob_filter_recent_vacancies() -> filter:
    all_vacancies = geekjob_get_vacancies_raw_data()
    today_str = datetime.datetime.today().strftime("%-d %B")
    filtered_vacancies = filter(
        lambda x: x["log"]["modify"] == today_str, all_vacancies
    )
    return filtered_vacancies


def geekjob_get_vacancy_html(vacancy_id: str) -> str:
    resp = requests.get(f"https://geekjob.ru/vacancy/{vacancy_id}")
    if resp.status_code != 200:
        return None
    return resp.text


def geekjob_get_vacancies_info() -> list:
    vacancies = []
    for item in geekjob_filter_recent_vacancies():
        vacancy_html = geek(item["id"])
        soup = BeautifulSoup(vacancy_html, features="html.parser")
        description = soup.find("div", id="vacancy-description").decode_contents()
        vacancy = {
            "id": "geekjob_" + item.get("id"),
            "company_name": item["company"]["name"],
            "title": item["position"],
            "salary": item["salary"],
            "location": item["city"],
            "speciality": item["speciality"],
            "internship": False,
            "remote": item["jobFormat"]["remote"],
            "url": f"https://geekjob.ru/vacancy/{item['id']}",
            "description": description,
        }
        if re.search(r"стажировк|internship", vacancy["description"], re.IGNORECASE):
            vacancy["internship"] = True
        vacancies.append(vacancy)
    return vacancies


if __name__ == "__main__":
    print("Импорт GeekJob")
    perform_import(geekjob_get_vacancies_info)
