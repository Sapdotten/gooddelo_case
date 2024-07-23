import aioredis

from aioredis import Redis

from app.redis_database.redis_settings import RedisSettings

from app.redis_database.redis_settings import RedisSettings


async def init_redis() -> Redis:
    redis = await aioredis.from_url(
        RedisSettings.get_redis_url(), decode_responses=True
    )
    return redis
