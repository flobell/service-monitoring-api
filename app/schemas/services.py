from pydantic import BaseModel


class ServiceCreate(BaseModel):
    name: str
    url: str
    check_interval: int = 60
