import logging

from sqlalchemy import text

from app.database.models import Base
from app.database.models import Base, User, Tokens, Task
from app.database.connect_db import engine

TABLES = [User, Tokens, Task]


async def init_models():
    async with engine.begin() as conn:
        tables_exists = True
        for table in TABLES:
            is_exist = await conn.execute(
                text(
                    "select exists(select 1 from information_schema.tables where table_name='users')"
                )
            )
            tables_exists = tables_exists and is_exist.fetchone()
        if tables_exists:
            logging.info("Db already exists")
        else:
            logging.info("Creating db...")

            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
            print("IS WORKING!")
