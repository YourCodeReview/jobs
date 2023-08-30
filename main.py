import requests
from bs4 import BeautifulSoup 
from requests.exceptions import HTTPError
import lxml

# URL = "https://hh.ru"
def split_serch_word(text):
    return text.split(" ")

search_vac = 'Стажер python'
area = 1 # Москва

URL = f"https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text={split_serch_word(search_vac)[0]}+{split_serch_word(search_vac)[1]}&excluded_text=&{area}&page=1"

session = requests.session()
session.headers = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0 (Edition Yx 05)",
    "accept-language": "en-US,en;q=0.9,ru;q=0.8,hy;q=0.7"
}

if __name__ == "__main__":
    try:
        res = session.get(URL)
        res.raise_for_status()
        html = res.text
        soup = BeautifulSoup(html, 'lxml')
        divs = soup.select("div.serp-item")
        for div in divs:
            print(div.select_one("a.serp-item__title").text)
    except HTTPError as ht:
        print(f"Error {ht}")        
    except Exception as ex:
        print(f"Error {ex}")