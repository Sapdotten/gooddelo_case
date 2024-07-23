import logging

from typing import Union

import hashlib

from app.database.models import User, Base, Tokens
from sqlalchemy import text, select

from app.database.connect_db import engine, async_session

hasher = hashlib.new('sha256')

async def init_models():
    async with engine.begin() as conn:
        is_exist = await conn.execute(
            text(
                "select exists(select 1 from information_schema.tables where table_name='users')"
            )
        )
        if is_exist.fetchone():
            logging.info("Db already exists")
        else:
            logging.info("Creating db...")
            
            
            await conn.run_sync(Base.metadata.create_all)
            print('IS WORKING!')
            
            
async def add_user(login: str, password: str) -> Union[int, None]:
    """Adds new user to db

    Args:
        login (str): login of user
        password (str): password of user

    Returns:
        bool: user_id if user has been added, None else
    """
    async with async_session() as session:
        user = await session.execute(select(User).where(User.login == login))
        user = user.scalars().first()
        if not user:
            new_user = User(login = login, password_hash=hasher.update(password.encode()))
            session.add(new_user)
            await session.commit()
            logging.info(f"User {login} was added to db")
            return new_user.id
        else:
            logging.info(f"User {login} wasn't added to the db")
            return None
            
            
async def add_token(user_id: int, token: str) -> int:
    async with async_session() as session:
        new_token = Tokens(refresh_token = token,
                            user_id = user_id)
        session.add(new_token)
        await session.commit()
        return new_token.id
        
async def delete_token(refresh_token_id: str) -> bool:
    async with async_session() as session:
        token = await session.execute(select(Tokens).where(Tokens.id==refresh_token_id))
        token = token.scalars().first()
        if token:
            await session.delete(token)
            await session.commit()
            return True
        else:
            return False
                
async def check_token(user_id: int, token: str)-> bool:
    async with async_session() as session:
        tokens = await session.execute(select(Tokens).where(Tokens.user_id==user_id))
        tokens = token.scalarc().all()
        for real_token in tokens:
            if real_token.refresh_token==token:
                return True
        return False
    
async def check_user(login: str, password: str) -> Union[int, None]:
    """Checks correct of login and password

    Args:
        login (str): login of user
        password (str): password of user

    Returns:
        Union[int, None]: int if data are correct, None else
    """
    async with async_session() as session:
        user = await session.execute(select(User).where(User.login==login))
        user = user.scalars().first()
        if user:
            if user.password_hash==hasher.update(password.encode()):
                return user.id
        return False
        
        
