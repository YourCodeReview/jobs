import requests
import lxml
import time
from bs4 import BeautifulSoup
from datetime import datetime


languages_stacks = [
    "python",
    "java",
    "javascript",
    "qa",
    "c#",
    "data scientist",
    "data science",
    "data analyst",
    "data engineer",
    "ml",
    "аналитик данных",
    "frontend",
    "backend",
]


def habr_find_vacancy_url(url):
    page = 0
    links_habr = []
    while True:
        page += 1
        params = {"page": page}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            if not soup.find("a", {"class": "vacancy-card__title-link"}):
                break

            link_elements = soup.find_all("a", {"class": "vacancy-card__title-link"})

            for link in link_elements:
                full_url = f"https://career.habr.com/{link['href']}"
                links_habr.append(full_url)

        else:
            print(f"Error {response.status_code}: Unable to retrieve the page content.")
    return links_habr


def habr_find_all_vacancy():
    url = "https://career.habr.com/vacancies?currency=RUR&qid=1&remote=1&s[]=2&s[]=3&s[]=82&s[]=4&s[]=5&s[]=72&s[]=1&s[]=75&s[]=6&s[]=77&s[]=7&s[]=83&s[]=84&s[]=8&s[]=85&s[]=73&s[]=9&s[]=86&s[]=106&s[]=12&s[]=10&s[]=13&s[]=11&s[]=87&s[]=14&s[]=15&s[]=16&s[]=107&s[]=41&s[]=98&s[]=42&s[]=99&s[]=43&s[]=44&s[]=76&s[]=96&s[]=97&s[]=95&s[]=100&s[]=111&s[]=94&s[]=23&s[]=24&s[]=30&s[]=25&s[]=27&s[]=26&s[]=90&s[]=91&s[]=28&s[]=92&s[]=29&s[]=93&s[]=31&s[]=109&s[]=32&s[]=33&s[]=34&s[]=119&s[]=35&s[]=36&s[]=37&s[]=70&s[]=38&s[]=39&s[]=71&s[]=110&s[]=78&s[]=79&s[]=80&s[]=81&s[]=118&s[]=21&s[]=22&s[]=17&s[]=18&s[]=19&s[]=20&s[]=89&s[]=108&s[]=51&s[]=53&s[]=120&s[]=113&s[]=121&s[]=103&s[]=102&s[]=104&s[]=52&sort=date&type=all"
    url_junior = "https://career.habr.com/vacancies?qid=3&remote=1&s[]=2&s[]=3&s[]=82&s[]=4&s[]=5&s[]=72&s[]=1&s[]=75&s[]=6&s[]=77&s[]=7&s[]=83&s[]=84&s[]=8&s[]=85&s[]=73&s[]=9&s[]=86&s[]=106&s[]=12&s[]=10&s[]=13&s[]=11&s[]=87&s[]=14&s[]=15&s[]=16&s[]=107&s[]=41&s[]=98&s[]=42&s[]=99&s[]=43&s[]=44&s[]=76&s[]=96&s[]=97&s[]=95&s[]=100&s[]=111&s[]=94&s[]=23&s[]=24&s[]=30&s[]=25&s[]=27&s[]=26&s[]=90&s[]=91&s[]=28&s[]=92&s[]=29&s[]=93&s[]=31&s[]=109&s[]=32&s[]=33&s[]=34&s[]=119&s[]=35&s[]=36&s[]=37&s[]=70&s[]=38&s[]=39&s[]=71&s[]=110&s[]=78&s[]=79&s[]=80&s[]=81&s[]=118&s[]=21&s[]=22&s[]=17&s[]=18&s[]=19&s[]=20&s[]=89&s[]=108&s[]=51&s[]=53&s[]=120&s[]=113&s[]=121&s[]=103&s[]=102&s[]=104&s[]=52&sort=date&type=all"
    links_habr = habr_find_vacancy_url(url)
    links_habr_junior = habr_find_vacancy_url(url_junior)
    links_habr.extend(links_habr_junior)
    return links_habr


def habr_get_vacancy_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        idx = url.split("/")[-1]
        site = url.split("/")[2]
        company_name = soup.find("div", {"class": "company_name"})
        title = soup.find("h1", {"class": "page-title__title"})
        salary = soup.find(
            "div", {"class": "basic-salary basic-salary--appearance-vacancy-header"}
        )
        specialities = map(
            lambda x: x.text,
            soup.findAll("a", {"class": "link-comp link-comp--appearance-dark"}),
        )
        speciality = None
        for spec in specialities:
            if spec == "Инженер по ручному тестированию":
                speciality = "qa"
                break
            if spec.lower() in languages_stacks:
                speciality = spec.lower()
                break
        description = soup.find("div", {"class": "vacancy-description__text"})
        date = soup.find('time', {'class': 'basic-date'})['datetime']
        vacancy = {
            "id": idx,
            "site": site,
            "company_name": company_name.text if company_name else None,
            "title": title.text if title else None,
            "salary": salary.text if salary else None,
            "speciality": speciality,
            "url": url,
            "description": description.decode_contents(),
            "location": None,
            "internship": False,
            "remote": False,
            "date_publication": datetime.fromisoformat(date) if date else None,
        }

        return vacancy
    else:
        print(f"Error {response.status_code}: Unable to retrieve the page content.")


def habr_get_vacancies_info():
    vacancies = []
    for url in habr_find_all_vacancy():
        vacancy = habr_get_vacancy_data(url)
        if vacancy:
            vacancies.append(vacancy)
    return vacancies


from database import get_db
from crud import create_vacancy
from parsing.hh import delete_duplicates


def import_vacancies():
    result = habr_get_vacancies_info()
    for db in get_db():
        for job in result:
            create_vacancy(db, job)


if __name__ == "__main__":
    start = time.time()
    import_vacancies()
    delete_duplicates()
    end = time.time()
    print(f"Время: {round((end - start) / 60)} мин.")
