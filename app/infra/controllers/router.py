from fastapi import APIRouter

from app.infra.controllers.user_controller import user_router

app_router = APIRouter(prefix='/app')
app_router.include_router(user_router)
