from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.workers.scheduler import start_scheduler
from app.api.v1 import PREFIX
from app.api.v1 import services
from app.api.v1 import metrics


@asynccontextmanager
async def lifespan(app: FastAPI):
    start_scheduler()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(services.router, prefix=PREFIX, tags=["services"])
app.include_router(metrics.router, prefix=PREFIX, tags=["metrics"])


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def read_health():
    return {"status": "ok"}
