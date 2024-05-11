import json
import re
import time

import requests
from bs4 import BeautifulSoup


def vacancy_validation(vacancy_title):
    languages_stacks = [
        "python",
        "java",
        "javascript",
        "qa",
        "c#",
        "data scientist",
        "data science",
        "data analyst",
        "frontend",
        "backend",
    ]

    stop_words = [
        "senior",
        "(senior)",
        "middle",
        "(middle)",
        "expert",
        "techlead",
        "tech lead",
        "teamlead",
        "team lead",
        "lead",
        "старший",
        "заместитель",
        "руководитель",
        "ведущий",
    ]

    if any(keyword in vacancy_title.lower() for keyword in languages_stacks):
        if any(stop_word in vacancy_title.lower() for stop_word in stop_words):
            return False
        return True
    else:
        return False


def parse_vacancy(vacancy):
    title = vacancy.find("h3", class_="base-search-card__title").text
    if not vacancy_validation(title):
        return None

    company_name = vacancy.find("h4", class_="base-search-card__subtitle").text
    title = vacancy.find("h3", class_="base-search-card__title").text
    location = vacancy.find("span", class_="job-search-card__location").text
    url_vacancy = vacancy.find(
        "a",
        class_="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]",
    ).get("href")

    pattern_before_position = r".{10}(?=\?position)"
    pattern_trackingid_position = r"trackingId=([^&]+)&trk"

    match_before_refid = re.search(pattern_before_position, url_vacancy)
    match_trackingid_position = re.search(pattern_trackingid_position, url_vacancy)

    ten_chars_before_refid = match_before_refid.group(0)
    tracking_id = match_trackingid_position.group(1)
    detail_url = f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{ten_chars_before_refid}?trackingId={tracking_id}"

    r_description = requests.get(detail_url)
    soup_detail = BeautifulSoup(r_description.text, "lxml")
    div_element = soup_detail.select_one(
        ".show-more-less-html__markup.show-more-less-html__markup--clamp-after-5"
    )

    r_text = []
    for tag in div_element.find_all(["p", "li"]):
        if tag.name == "li":
            r_text.append("• " + tag.get_text())
        else:
            r_text.append(tag.get_text())

    vacancy = {
        "company_name": company_name.strip(),
        "title": title.strip(),
        "location": location.strip(),
        "url": url_vacancy,
        "description": r_text,
    }

    with open("all_link_vacancy.json", "a", encoding="utf-8") as json_file:
        json.dump(vacancy, json_file, indent=4, ensure_ascii=False)


def parse_one_page(all_vacancy_on_page):
    for vacancy in all_vacancy_on_page:
        parse_vacancy(vacancy)


def parse_all_page():
    start = 0
    while start < 1000:
        url = (
            "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=&location=&geoId=101728296&trk=guest_homepage-basic_jobs-search-bar_search-submit&start="
            + str(start)
        )
        print(f"Обрабатывается страница {url}")
        r = requests.get(url)
        print(f"Status Code: {r.status_code}")
        print(f"Status Message: {r.reason}")
        soup = BeautifulSoup(r.text, "lxml")
        all_vacancy_on_page = soup.findAll(
            "div",
            class_="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card",
        )
        parse_one_page(all_vacancy_on_page)
        start += 25
        time.sleep(1)
    start = 0
    print("Начинаю поиск по Беларуси")
    while start < 1000:
        url = (
            "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=&location=&geoId=101705918&trk=public_jobs_jobs-search-bar_search-submit&start="
            + str(start)
        )
        print(f"Обрабатывается страница {url}")
        r = requests.get(url)
        print(f"Status Code: {r.status_code}")
        print(f"Status Message: {r.reason}")
        soup = BeautifulSoup(r.text, "lxml")
        all_vacancy_on_page = soup.findAll(
            "div",
            class_="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card",
        )
        parse_one_page(all_vacancy_on_page)
        start += 25
        time.sleep(1)


