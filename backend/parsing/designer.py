import requests
import time
from bs4 import BeautifulSoup


def get_max_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    div_pages = soup.find("div", {"class": "blog-page-navigation"})
    max_page = div_pages.find_all("a")[-2].text
    return int(max_page)


def find_all_vacancy():
    url = "https://designer.ru/u/"
    # max_page = get_max_page(url)
    max_page = 1
    links_designer = []
    for i in range(1, max_page + 1):
        params = {"PAGEN_1": i}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            if not soup.find(
                "div",
                {
                    "class": "uk-width-large-1-4 uk-width-medium-1-3 uk-width-small-1-1 uk-margin-large-bottom"
                },
            ):
                break

            link_elements = soup.find_all(
                "div",
                {
                    "class": "uk-width-large-1-4 uk-width-medium-1-3 uk-width-small-1-1 uk-margin-large-bottom"
                },
            )

            for link in link_elements:
                link_a = link.find("a")
                full_url = f"https://designer.ru{link_a['href']}"
                links_designer.append(full_url)

        else:
            print(f"Error {response.status_code}: Unable to retrieve the page content.")
    return links_designer


def designer_create_vacancy(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        site = url.split("/")[2]
        company_name = soup.find("div", {"class": "z_b_72194kjs___intro_v2__www"})
        title = soup.find("div", {"class": "z_b_72194kjs___head_v2"}).parent.find("h1")
        salary = soup.find("div", {"class": "z_b_72194kjs___intro_v2__salary"})
        speciality = "Дизайнер"
        description_intro_v2 = soup.find("div", {"class": "z_b_72194kjs___intro_v2"})
        description_body = soup.find_all("div", {"class": "z_dtl_text_block_v3"})[:-1]
        combined_description = soup.new_tag("div")
        combined_description.append(description_intro_v2)

        for element in description_body:
            combined_description.append(element)

        vacancy = {
            "id": url.split("/")[-2],
            "site": site,
            "company_name": company_name.text if company_name else None,
            "title": title.text if title else None,
            "salary": salary.text if salary else None,
            "speciality": speciality,
            "url": url,
            "description": combined_description.decode_contents(),
            "location": " ",
            "speciality": "Design",
            "internship": False,
            "remote": False,
        }

        return vacancy
    else:
        print(f"Error {response.status_code}: Unable to retrieve the page content.")


def designer_get_vacancies_info():
    vacancies = []
    for url in find_all_vacancy():
        vacancy = designer_create_vacancy(url)
        if vacancy:
            vacancies.append(vacancy)
    return vacancies


from database import get_db
from crud import create_vacancy
from parsing.hh import delete_duplicates


def import_vacancies():
    result = designer_get_vacancies_info()
    for db in get_db():
        for job in result:
            create_vacancy(db, job)


if __name__ == "__main__":
    start = time.time()
    import_vacancies()
    delete_duplicates()
    end = time.time()
    print(f"Время: {round((end - start) / 60)} мин.")
