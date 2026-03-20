from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.services import Service
from app.schemas.services import ServiceCreate

router = APIRouter()


@router.post("/services")
def create_service(service: ServiceCreate, db: Session = Depends(get_db)):
    new_service = Service(**service.model_dump())
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service
