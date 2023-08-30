import scrapy

class BookSpyder(scrapy.Spider):
    name = "BookSider"
    def start_requests(self):
        vacancies = (f"https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=junior+python&excluded_text=&area=1&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&page={page}")
        start_urls = []

        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    pass