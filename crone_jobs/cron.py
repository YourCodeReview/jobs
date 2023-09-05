import cronitor.celery
from celery import Celery
from parsing import fetch_hh_page_vacancies

app = Celery()
app.conf.beat_schedule = {
    'run-me-every-minute': {
        'task': 'tasks.every_minute_celery_task',
        'schedule': 60
    }
}

# Discover all of your celery tasks and automatically add monitoring. 
cronitor.celery.initialize(app, api_key="apiKey123")

@app.task
def every_minute_celery_task():
    return "running a background job with celery..."

# @app.task
# def non_scheduled_celery_task():
#     print("Even though I'm not on a schedule, I'll still be monitored!")