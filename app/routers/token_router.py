from fastapi import APIRouter, Request, HTTPException, Depends
from app.routers.models import token_models
from fastapi.security import OAuth2PasswordBearer
from app.routers.limiter import limiter
from app.utils.tokens import TokenManager
from app.database.managers import user_manager

router = APIRouter(
    prefix="",
    tags=["Работа с пользователями"],
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/token/refresh", response_model=token_models.RefreshTokenSuccessResponse)
@limiter.limit("100/minute")
async def refresh_token(request: Request, token: token_models.RefreshTokenRequest):
    payload = TokenManager.decode_token(token.refresh_token)
    if payload:
        user_id = payload["user_id"]
    else:
        raise HTTPException(status_code=401, detail="Refresh token is not valid")
    try:
        refresh_token_id = await user_manager.check_token(user_id, token.refresh_token)
        if refresh_token_id:
            new_token = TokenManager.create_access_token(user_id, refresh_token_id)
            return token_models.RefreshTokenSuccessResponse(
                access_token=new_token,
                expires_in=TokenManager.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            )
        else:
            raise HTTPException(status_code=401, detail="Refresh token is not valid")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
