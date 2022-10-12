from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import parse_active_calls


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(parse_active_calls, 'interval', seconds=2)
    scheduler.start()
