from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, HttpUrl


class TestRunRequest(BaseModel):
    url: HttpUrl
    method: str = Field(default="GET")
    headers: Optional[Dict[str, str]] = None
    body: Optional[Dict[str, Any]] = None
    request_count: int = Field(default=10, ge=1, le=500)
    concurrency: int = Field(default=5, ge=1, le=50)
    timeout: float = Field(default=5.0, gt=0, le=30)