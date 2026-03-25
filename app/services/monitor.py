import requests
import time
from app.db.session import SessionLocal
from app.db.models.services import Service
from app.db.models.metrics import Metric


def check_service(service):
    start = time.time()

    try:
        response = requests.get(service.url, timeout=5)
        duration = int((time.time() - start) * 1000)

        status = "UP" if response.status_code == service.expected_status else "DOWN"

        return {
            "status": status,
            "status_code": response.status_code,
            "response_time_ms": duration,
            "error_message": None
        }

    except Exception as e:
        return {
            "status": "DOWN",
            "status_code": None,
            "response_time_ms": None,
            "error_message": str(e)
        }


def check_all_services():
    db = SessionLocal()

    services = db.query(Service).filter(Service.is_active == True).all()
    print(f"Checking {len(services)} services...")
    for service in services:
        result = check_service(service)

        metric = Metric(
            service_id=service.id,
            **result
        )

        db.add(metric)

    db.commit()


def get_consecutive_failures(db, service_id, limit=3):
    metrics = (
        db.query(Metric)
        .filter(Metric.service_id == service_id)
        .order_by(Metric.checked_at.desc())
        .limit(limit)
        .all()
    )

    failures = 0

    for m in metrics:
        if m.status == "DOWN":
            failures += 1
        else:
            break

    return failures
