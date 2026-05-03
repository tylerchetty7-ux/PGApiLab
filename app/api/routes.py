from fastapi import APIRouter
from app.schemas.test_run import TestRunRequest
from app.services.load_tester import send_single_request

router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "PGApiLab"
    }


@router.post("/tests/run")
async def run_test(request: TestRunRequest):
    result = await send_single_request(
        url=str(request.url),
        method=request.method,
        headers=request.headers,
        body=request.body,
        timeout=request.timeout
    )

    return {
        "message": "Single request test completed",
        "target": str(request.url),
        "method": request.method,
        "result": result
    }