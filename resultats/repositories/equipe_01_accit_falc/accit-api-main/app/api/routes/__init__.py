from fastapi import APIRouter

from .falc import router as router_falc

api_router = APIRouter()
api_router.include_router(router_falc, tags=["falc"])
