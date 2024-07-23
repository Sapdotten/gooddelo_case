from string import Template

from app.utils.settings import Settings

class DBSettings:
     CONNECT_STRING = Template("postgresql+asyncpg://${user}:${password}@${hostname}/${dbname}")
     
     @classmethod
     def get_url(cls) -> str:
         URL =  cls.CONNECT_STRING.substitute(
             user = Settings.get_sql_user(),
             password = Settings.get_sql_password(),
             hostname = Settings.get_sql_host(),
             dbname = Settings.get_sql_db_name()
         )
         print(URL)
         return URL