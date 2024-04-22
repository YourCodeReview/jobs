# LinkedIn vacancy parser v.1.1
Alpha version of my LinkedIn job vacancy parser, utilizing the Scrapy framework.

Description:
- The parser loads pages containing lists of job vacancies for selected regions (Russia and Belarus).
- It scrolls through all vacancies and identifies those matching specified technology stacks and difficulty levels (grind).
- Essential data about the vacancies is collected.
- The obtained vacancies are saved in a file named vacancy_list.json.

# Getting Started

1. Clone this project https://github.com/Valpydeveloper/LinkedInParser.git
2. Create a Python Virtual Environment: `python3 -m venv venv`
3. Activate the Python Virtual Environment: `source venv/bin/activate`
4. Install requirements.txt: `pip install -r requirements.txt`
5. Listing the scrapy projects `scrapy list` 
6. Running the scrapy project: `scrapy crawl linkedin_jobs` 




