from fastapi import FastAPI
from app.api.v1 import services


app = FastAPI()

app.include_router(services.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def read_health():
    return {"status": "ok"}
