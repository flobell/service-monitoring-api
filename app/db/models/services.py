from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    expected_status = Column(Integer, default=200)
    check_interval = Column(Integer, default=60)
    is_active = Column(Boolean, default=True)
