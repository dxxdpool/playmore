from app.api.routes.health_check_route import router as health_router
from fastapi import FastAPI

app = FastAPI(
    title="Playmore Backend",
    description="Backend for sports session scheduling and waitlist management",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.include_router(health_router)
