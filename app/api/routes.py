from fastapi import APIRouter
from app.schemas.test_run import TestRunRequest
from app.services.load_tester import run_sequential_test

router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "PGApiLab"
    }


@router.post("/tests/run")
async def run_test(request: TestRunRequest):
    test_result = await run_sequential_test(
        url=str(request.url),
        method=request.method,
        headers=request.headers,
        body=request.body,
        request_count=request.request_count,
        timeout=request.timeout
    )

    return {
        "message": "Sequential test completed",
        "target": str(request.url),
        "method": request.method,
        "concurrency": request.concurrency,
        "data": test_result
    }