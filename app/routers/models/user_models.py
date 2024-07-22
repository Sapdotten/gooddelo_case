from pydantic import BaseModel


class RegisterUserModel(BaseModel):
   login: str
   password: str
   email: str