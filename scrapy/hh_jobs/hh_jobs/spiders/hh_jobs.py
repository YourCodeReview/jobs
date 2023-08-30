# from pathlib import Path

import scrapy


class HH_Jobs(scrapy.Spider):
    name = "hh_jobs"

    def start_requests(self):
        urls = [
            "https://hh.ru/search/vacancy",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # vac = response.css("a.serp-item__title::text").get()
        # salary = response.css("span.bloko-header-section-2::text").get().replace('\u202f', '').split(' – ')
