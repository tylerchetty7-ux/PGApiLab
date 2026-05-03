from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="PGApiLab",
    description="API latency and reliability testing platform",
    version="0.1.0"
)

app.include_router(router)