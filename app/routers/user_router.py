from fastapi import APIRouter
from routers.limiter import limiter
router = APIRouter(
   prefix="/",
   tags=["Работа с пользователями"],
)


@router.post("/register")
@limiter.limit("100/minute")
async def register_user():
   pass

@router.post("/login")
@limiter.limit("100/minute")
async def login_user():
   pass

@router.post("/logout")
@limiter.limit("100/minute")
async def logout_user():
   pass