from fastapi import APIRouter, Request
from app.routers.models import user_models
from app.routers.limiter import limiter


router = APIRouter(
   prefix="",
   tags=["Работа с пользователями"],
)


@router.post("/register")
@limiter.limit("100/minute")
async def register_user(request: Request, user_data: user_models.RegisterUserModel):
   return {"data": user_data}

@router.post("/login")
@limiter.limit("100/minute")
async def login_user(request: Request):
   pass

@router.post("/logout")
@limiter.limit("100/minute")
async def logout_user(request: Request):
   pass