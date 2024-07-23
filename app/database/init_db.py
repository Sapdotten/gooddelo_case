import logging


from app.database.models import Base
from sqlalchemy import text, select

from app.database.connect_db import engine


async def init_models():
    async with engine.begin() as conn:
        # is_exist = await conn.execute(
        #     text(
        #         "select exists(select 1 from information_schema.tables where table_name='users')"
        #     )
        # )
        # if is_exist.fetchone():
        #     logging.info("Db already exists")
        # else:
        #     logging.info("Creating db...")
            
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        print('IS WORKING!')