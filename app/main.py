from contextlib import asynccontextmanager

from fastapi import FastAPI
from slowapi import _rate_limit_exceeded_handler

from slowapi.errors import RateLimitExceeded

from app.routers.limiter import limiter
from app.routers import task_router, user_router, token_router
from app.database.init_db import init_models
from app.redis_database import init_redis


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_models()
    task_router.redis = await init_redis.init_redis()
    yield


app = FastAPI(lifespan=lifespan)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.include_router(task_router.router)
app.include_router(user_router.router)
app.include_router(token_router.router)
