import os
import time

import psycopg2

from crud import create_vacancy
from models import Vacancy
from database import get_db


def get_duplicates(session, external_ids):
    existing = session.query(Vacancy.id, Vacancy.external_id) \
        .filter(Vacancy.external_id.in_(external_ids)) \
        .all()
    return existing


def import_new_vacancies(vacancies):
    external_ids = [v["id"] for v in vacancies]
    count_new = 0
    count_existing = 0
    for db in get_db():
        existing = get_duplicates(db, external_ids)
        existing = [item[1] for item in existing]
        for vacancy in vacancies:
            if vacancy["id"] not in existing:
                create_vacancy(db, vacancy)
                count_new += 1
            else:
                count_existing += 1
    print(f"Новых {count_new}, существующих {count_existing}")
    return count_new


def perform_import(import_func):
    imported_count = None
    start = time.time()
    try:
        result = import_func()
        imported_count = import_new_vacancies(result)
    except Exception as e:
        print(f"Ошибка {e}")
        raise
    else:
        print(f"Импортировано вакансий: {imported_count}")
    finally:
        end = time.time()
        print(f"Время: {round((end - start) / 60)} мин.")


def clear_db():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )

        cur = conn.cursor()

        cur.execute("DELETE FROM vacancies;")

        conn.commit()

        cur.close()
        conn.close()
    except Exception as e:
        print("Error: ", str(e))
