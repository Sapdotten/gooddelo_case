from typing import Union

from app.database.models import Task
from sqlalchemy import select

from app.database.connect_db import async_session


async def add_new_task(user_id: int, task: str) -> int:
    """Adds new note to db

    Args:
        user_id (int): id of user in db
        note (str): text of note

    Returns:
        int: id of new note
    """
    async with async_session() as session:
        new_note = Task(user_id=user_id, task=task)
        session.add(new_note)
        await session.commit()
        return new_note.id


async def get_all_tasks(user_id: int) -> list[dict[int, str]]:
    """Returns all tasks of user

    Args:
        user_id (int): _description_

    Returns:
        list[dict[int, str]]: list of dicts {"task_id": int, "task": str }
    """
    async with async_session() as session:
        tasks = await session.execute(select(Task).where(Task.user_id == user_id))
        tasks = tasks.scalars().all()
        if tasks:
            return [{"task_id": i.id, "task_text": i.task} for i in tasks]
        else:
            return []


async def get_task(user_id: int, task_id: int) -> Union[str, None]:
    """Finds a note by its id

    Args:
        user_id (int): id of user
        task_id (int): id of task

    Returns:
        Union[str, None]: text of task or None if it hasn't been found
    """
    async with async_session() as session:
        task = await session.execute(
            select(Task).where(Task.id == task_id and Task.user_id == user_id)
        )
        task = task.scalars().first()
        if task:
            return task.task
        else:
            return None


async def edit_task(user_id: int, task_id: int, task_text: str) -> bool:
    async with async_session() as session:
        task = await session.execute(
            select(Task).where(Task.id == task_id and Task.user_id == user_id)
        )
        task = task.scalars().first()
        if task:
            task.task = task_text
            await session.commit()
            return True
        else:
            return False


async def delete_task(user_id: int, task_id: int) -> bool:
    async with async_session() as session:
        task = await session.execute(
            select(Task).where(Task.id == task_id and Task.user_id == user_id)
        )
        task = task.scalars().first()
        if task:
            await session.delete(task)
            await session.commit()
            return True
        else:
            return False
