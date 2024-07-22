import os

class Settings:
    """Class that gets data from environment
    """
    _JWT_SECRET = "JWT_SECRET"
    _SQL_USER="SQL_USER"
    _SQL_PASSWORD="SQL_PASSWORD"
    _SQL_HOSTNAME="SQL_HOSTNAME"
    _SQL_DATABASE_NAME="SQL_DATABASE_NAME"
    _REDIS_HOST = "REDIS_HOST"
    _REDIS_PORT = "REDIS_PORT"
    _REDIS_DB = "REDIS_DB"
    
    @classmethod
    def get_jwt_secret(cls):
        return os.getenv(cls._JWT_SECRET)
    @classmethod
    def get_sql_user(cls):
        return os.getenv(cls._SQL_USER)

    @classmethod
    def get_sql_password(cls):
        return os.getenv(cls._SQL_PASSWORD)
    
    @classmethod
    def get_sql_host(cls):
        return os.getenv(cls._SQL_HOSTNAME)
    
    @classmethod
    def get_sql_db_name(cls):
        return os.getenv(cls._SQL_DATABASE_NAME)
    @classmethod
    def get_redis_host(cls):
        return os.getenv(cls._REDIS_HOST)
    
    @classmethod
    def get_redis_port(cls):
        return os.getenv(cls._REDIS_PORT)
    
    @classmethod
    def get_redis_db(cls):
        return os.getenv(cls._REDIS_DB)