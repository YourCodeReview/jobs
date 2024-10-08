import re
import time
from bs4 import BeautifulSoup
from parsing.utils import perform_import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


def jobby_get_vacancies_raw_data() -> list:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-dev-shm-usage")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    raw_data = []

    try:
        url = "https://jobby.ai/student_jobsearch_m?area=&employment=&industrie=&profarea=7&employ=&page=1&pagemin=&schedule=&global=%D0%BD%D0%B5%D1%82&experience=yes&area_p=&specialization=52%2C%2054%2C%2055%2C%2058%2C%2059%2C%2060%2C%2061%2C%2062%2C%2063%2C%2064%2C%2065%2C%2067%2C%2050%2C%2049%2C%2048%2C%2047%2C%2045%2C%2044%2C%2043%2C%2053&one_year_experience=no&isFirst=no&country="
        driver.get(url)
        clickable_div_class = "div.clickable-element.bubble-element.Group.coaArh1.bubble-r-container.flex.column"
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, clickable_div_class))
        )

        original_window = driver.current_window_handle
        remaining_elements = driver.find_elements(By.CSS_SELECTOR, clickable_div_class)

        for remaining_element in remaining_elements:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, clickable_div_class))
            )
            remaining_element.click()
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

            for window_handle in driver.window_handles:
                if window_handle != original_window:
                    driver.switch_to.window(window_handle)
                    break

            new_page_url = driver.current_url
            time.sleep(1)
            page_source = driver.page_source
            raw_data.append((new_page_url, page_source))

            driver.close()
            driver.switch_to.window(original_window)
    except Exception as e:
        print(f'jobby raw data exception {str(e)}')
    finally:
        driver.quit()
    return raw_data


def jobby_get_vacancies_info() -> list:
    vacancies = []
    for url, page_source in jobby_get_vacancies_raw_data():
        vacancy_html = page_source
        soup = BeautifulSoup(vacancy_html, features="html.parser")
        description = soup.find("div", class_="coaSaaB2").decode_contents()
        vacancy = {
            "id": "jobby_" + re.search("vacancy=([^&]+)", url).group(1),
            "company_name": soup.find("div", class_="coaSbaJ2").text,
            "title": soup.find("h1", class_="coaSam2").text,
            "salary": soup.find("div", class_="coaSbaC2").text,
            "location": soup.find(
                "div",
                class_="coaSck2".split(),
            ).text,
            "speciality": " ",
            "internship": False,
            "remote": False,
            "url": url,
            "description": description,
        }
        if re.search(
            r"удал[её]нная работа|удал[её]нн|удал[её]нк",
            vacancy["description"],
            re.IGNORECASE,
        ):
            vacancy["remote"] = True
        if re.search(r"стажировк|internship", vacancy["description"], re.IGNORECASE):
            vacancy["internship"] = True
        vacancies.append(vacancy)
    return vacancies


if __name__ == "__main__":
    print("Импорт Jobby")
    perform_import(jobby_get_vacancies_info)
