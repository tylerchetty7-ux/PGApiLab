import time
from typing import Any, Dict, Optional

import httpx


async def send_single_request(
    url: str,
    method: str,
    headers: Optional[Dict[str, str]],
    body: Optional[Dict[str, Any]],
    timeout: float
) -> Dict[str, Any]:
    start_time = time.perf_counter()

    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.request(
                method=method,
                url=url,
                headers=headers,
                json=body
            )

        end_time = time.perf_counter()
        latency_ms = (end_time - start_time) * 1000

        return {
            "success": response.status_code < 400,
            "status_code": response.status_code,
            "latency_ms": round(latency_ms, 2),
            "error": None
        }

    except httpx.TimeoutException:
        end_time = time.perf_counter()
        latency_ms = (end_time - start_time) * 1000

        return {
            "success": False,
            "status_code": None,
            "latency_ms": round(latency_ms, 2),
            "error": "Request timed out"
        }

    except httpx.RequestError as error:
        end_time = time.perf_counter()
        latency_ms = (end_time - start_time) * 1000

        return {
            "success": False,
            "status_code": None,
            "latency_ms": round(latency_ms, 2),
            "error": str(error)
        }

async def run_sequential_test(
    url: str,
    method: str,
    headers: Optional[Dict[str, str]],
    body: Optional[Dict[str, Any]],
    request_count: int,
    timeout: float
) -> Dict[str, Any]:
    results = []

    for _ in range(request_count):
        result = await send_single_request(
            url=url,
            method=method,
            headers=headers,
            body=body,
            timeout=timeout
        )

        results.append(result)

    return {
        "request_count": request_count,
        "results": results
    }