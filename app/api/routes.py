from fastapi import APIRouter
from app.schemas.test_run import TestRunRequest

router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "PGApiLab"
    }


@router.post("/tests/run")
def run_test(request: TestRunRequest):
    return {
        "message": "Request validated successfully",
        "data": request
    }