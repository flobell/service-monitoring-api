from apscheduler.schedulers.background import BackgroundScheduler
from app.services.monitor import check_all_services

scheduler = BackgroundScheduler()


def start_scheduler():
    scheduler.add_job(check_all_services, "interval", seconds=60)
    scheduler.start()
