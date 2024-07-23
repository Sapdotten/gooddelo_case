from app.utils.settings import Settings


class RedisSettings:
    _URL_START = "redis://"

    @classmethod
    def get_redis_url(cls) -> str:
        """Returns an url for connect to redis

        Returns:
            str: url
        """
        url = "" + cls._URL_START

        redis_user = Settings.get_redis_user()
        redis_db = Settings.get_redis_db()
        if redis_user:
            redis_password = Settings.get_redis_password()
            url += redis_user + ":" + redis_password + "@"
        url += "localhost"
        if redis_db:
            url += "/" + redis_db
        return url
