from app.db.deps import get_db
from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

router = APIRouter()


@router.get(
    "/health_check",
    summary="Check server health",
    description="Returns OK if server is running",
)
def health_check():
    return {"status": "ok"}


@router.get(
    "/health_check/db",
    summary="Check DB connection",
    description="Returns OK if DB is connected",
)
def health_db(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"database": "connected"}
