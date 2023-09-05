import cronitor.celery
from celery import Celery
import cronitor

cronitor.api_key = 'b8cb4f4c7a09431bbb44bcd118e5500f'


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