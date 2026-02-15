from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/health_check",
    summary="Check server health",
    description="Returns OK if server is running",
)
def health_check():
    return {"status": "ok"}
