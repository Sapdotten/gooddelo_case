import jwt

from datetime import datetime, timedelta, timezone
from typing import Union

from app.utils.settings import Settings


class TokenManager:
    __SECRET_KEY = Settings.get_jwt_secret()
    (
        ALGORITHM,
        ACCESS_TOKEN_EXPIRE_MINUTES,
        REFRESH_TOKEN_EXPIRE_DAYS,
    ) = Settings.get_jwt_configs()

    header = {"alg": ALGORITHM, "typ": "JWT"}

    @classmethod
    def create_access_token(cls, user_id: int, refresh_token_id: int):
        payload = {"user_id": user_id, "refresh_token_id": refresh_token_id}
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=cls.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        payload["exp"] = expire
        encoded_jwt = jwt.encode(payload, cls.__SECRET_KEY, algorithm=cls.ALGORITHM)
        return encoded_jwt

    @classmethod
    def create_refresh_token(cls, user_id: int):
        payload = {"user_id": user_id}
        expire = datetime.now(timezone.utc) + timedelta(
            days=cls.REFRESH_TOKEN_EXPIRE_DAYS
        )
        payload["exp"] = expire
        encoded_jwt = jwt.encode(payload, cls.__SECRET_KEY, algorithm=cls.ALGORITHM)
        return encoded_jwt

    @classmethod
    def decode_token(cls, token: str) -> Union[None, dict]:
        try:
            decoded_token = jwt.decode(
                token, cls.__SECRET_KEY, algorithms=[cls.ALGORITHM]
            )
            return (
                decoded_token
                if decoded_token["exp"] >= datetime.now(timezone.utc).timestamp()
                else None
            )
        except jwt.ExpiredSignatureError:
            return None
        except jwt.PyJWTError:
            return None
