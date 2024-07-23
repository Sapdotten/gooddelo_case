import logging

from sqlalchemy.ext.asyncio import create_async_engine
from app.database.db_settings import DBSettings
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession


engine = create_async_engine(url=DBSettings.get_url(), max_overflow=10, echo=True)
logging.info("Engine for database is initialized")
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
logging.info("async_session is created")