from fastapi import APIRouter

router = APIRouter(
   prefix="/",
   tags=["Работа с пользователями"],
)


@router.post("/register")
async def register_user():
   pass

@router.post("/login")
async def login_user():
   pass

@router.post("/logout")
async def logout_user():
   pass