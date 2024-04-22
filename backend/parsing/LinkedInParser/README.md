# LinkedIn vacancy parser v.1.1
Alpha version of my LinkedIn job vacancy parser, utilizing the Scrapy framework.

Description:
- The parser loads pages containing lists of job vacancies for selected regions (Russia and Belarus).
- It scrolls through all vacancies and identifies those matching specified technology stacks and difficulty levels (grind).
- Essential data about the vacancies is collected.
- The obtained vacancies are saved in a file named vacancy_list.json.

# Getting Started

1. Write in terminal `cd backend/parsing/LinkedInParser/linkedin_spider`
6. Running the scrapy project: `scrapy crawl linkedin_jobs` 




