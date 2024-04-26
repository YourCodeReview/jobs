import scrapy
import json
import re


class LinkedJobsSpider(scrapy.Spider):
    name = "linkedin_jobs"

    # api url - ссылка на вакансии по России
    # api two - ссылка на вакансии по Беларуси
    api_url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=&location=&geoId=101728296&trk=guest_homepage-basic_jobs-search-bar_search-submit&start="
    api_two = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=&location=&geoId=101705918&trk=public_jobs_jobs-search-bar_search-submit&start="

    def start_requests(self):
        """
        Генерирует начальные запросы для сбора данных о вакансиях.

        Этот метод вызывается при запуске паука. Он конструирует первый URL для сбора данных о вакансиях
        и возвращает объект `scrapy.Request` для получения данных с указанного URL.

        Аргументы:
            self: Экземпляр паука.

        Возвращает:
            scrapy.Request: Объект запроса для получения данных о вакансиях с указанного URL.
        """

        first_job_on_page = 0
        first_url = self.api_url + str(first_job_on_page)
        print(f"Стартовая страница {first_job_on_page}")
        yield scrapy.Request(
            url=first_url,
            callback=self.parse_job,
            meta={"first_job_on_page": first_job_on_page},
        )

    def vacancy_validation(self, vacancy_title):
        """
        Проверяет валидность заголовка вакансии на основе ключевых слов и стоп-слов.

        Этот метод используется для фильтрации вакансий. Он проверяет, содержит ли заголовок вакансии
        ключевые слова, связанные с языками программирования и технологическими стеками. Также метод
        исключает вакансии, содержащие стоп-слова, которые указывают на определенные уровни (например, "senior",
        "middle") или роли (например, "lead", "руководитель").

        Аргументы:
            self: Экземпляр паука.
            vacancy_title (str): Заголовок вакансии для проверки.

        Возвращает:
            bool: True, если заголовок вакансии валиден, иначе False.
        """

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
            # Проверяем, есть ли хотя бы одно стоп-слово в заголовке вакансии
            if any(stop_word in vacancy_title.lower() for stop_word in stop_words):
                return False
            return True
        else:
            return False

    def parse_job(self, response):
        """
        Этот метод извлекает со страницы информацию о вакансиях. Он получает данные о компании,
        названии вакансии, местоположении, URL и дате публикации. Также метод использует функцию
        `vacancy_validation` для проверки валидности заголовка вакансии.

        Аргументы:
            self: Экземпляр паука.
            response (scrapy.http.Response): Ответ, содержащий вакансии.
        """

        first_job_on_page = response.meta["first_job_on_page"]

        # job_item словарь, в который вносятся вакансии, на сайте вакансии находятся в теге "li". Таких тегов нам отдает примерно по 25 штук со страницы
        jobs = response.css("li")

        num_jobs_returned = len(jobs)
        print("******* Вакансий обнаружено *******")
        print(num_jobs_returned)
        print("********************************")

        for job in jobs:
            vacancy_title = job.css("h3::text").get(default="not-found").strip()
            result = self.vacancy_validation(vacancy_title)

            if result:
                job_item = {
                    "company_name": job.css("h4 a::text")
                    .get(default="not-found")
                    .strip(),
                    "title": vacancy_title,
                    "location": job.css(".job-search-card__location::text")
                    .get(default="not-found")
                    .strip(),
                    "url": job.css(".base-card__full-link::attr(href)")
                    .get(default="not-found")
                    .strip(),
                    "published": job.css("time::text").get(default="not-found").strip(),
                }

                pattern_before_refid = r".{10}(?=\?refId)"
                pattern_trackingid_position = r"trackingId=([^&]+)&position"

                match_before_refid = re.search(pattern_before_refid, job_item["url"])
                match_trackingid_position = re.search(
                    pattern_trackingid_position, job_item["url"]
                )

                if match_before_refid and match_trackingid_position:
                    ten_chars_before_refid = match_before_refid.group(0)
                    tracking_id = match_trackingid_position.group(1)
                    detail_url = f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{ten_chars_before_refid}?trackingId={tracking_id}"

                    yield scrapy.Request(
                        detail_url,
                        callback=self.parse_detail,
                        meta={"job_item": job_item},
                    )

        if num_jobs_returned > 0:
            first_job_on_page = int(first_job_on_page) + 25
            next_url = self.api_url + str(first_job_on_page)
            print(f"Обработано {first_job_on_page} вакансий")
            yield scrapy.Request(
                url=next_url,
                callback=self.parse_job,
                meta={"first_job_on_page": first_job_on_page},
            )
        else:
            self.api_url = self.api_two
            first_job_on_page = 0
            next_url = self.api_url + str(first_job_on_page)
            print("Поиск вакансий по РФ закончен, начинаю поиск вакансий по РБ")
            yield scrapy.Request(
                url=next_url,
                callback=self.parse_job,
                meta={"first_job_on_page": first_job_on_page},
            )

    def parse_detail(self, response):

        """
        Этот метод извлекает дополнительные детали о вакансии со страницы деталей вакансии.
        Он извлекает текст из различных элементов (параграфов, списков и т. д.) и сохраняет его
        в поле "description" в объекте вакансии. Затем метод записывает вакансию в файл
        "vacancy_list3.json".

        Аргументы:
            self: Экземпляр паука.
            response (scrapy.http.Response): Ответ, содержащий детали вакансии.
        """

        job_item = response.meta["job_item"]

        all_text = response.css(
            ".show-more-less-html__markup.show-more-less-html__markup--clamp-after-5 p::text, .show-more-less-html__markup.show-more-less-html__markup--clamp-after-5 p br::text, .show-more-less-html__markup.show-more-less-html__markup--clamp-after-5 p strong::text, .show-more-less-html__markup.show-more-less-html__markup--clamp-after-5 ul li::text"
        ).getall()
        ul_text = response.css(
            ".show-more-less-html__markup.show-more-less-html__markup--clamp-after-5 ul li::text"
        ).getall()

        for i in range(len(all_text)):
            if all_text[i] in ul_text:
                all_text[i] = f"• {all_text[i]}"

        job_item["description"] = all_text

        with open("vacancy_list.json", "a", encoding="utf-8") as json_file:
            json.dump(job_item, json_file, indent=4, ensure_ascii=False)

        yield job_item
