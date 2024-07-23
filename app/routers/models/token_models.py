from pydantic import BaseModel


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class RefreshTokenSuccessResponse(BaseModel):
    access_token: str
    expires_in: int
