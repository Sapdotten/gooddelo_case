from fastapi import APIRouter

router = APIRouter(
   prefix="/",
   tags=["Работа с пользователями"],
)


@router.post("/register")
def register_user():
   pass

@router.post("/login")
def login_user():
   pass

@router.post("/logout")
def logout_user():
   pass