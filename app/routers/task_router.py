from fastapi import FastAPI
from fastapi import APIRouter

router = APIRouter(
   prefix="/tasks",
   tags=["Записи"],
)


@router.post("/")
async def create_note():
   pass

@router.get("/")
async def get_all_notes():
   pass

@router.get("/{task_id}")
async def get_note(task_id):
   pass

@router.put("/{task_id}")
async def edit_note(task_id):
   pass

@router.delete("/{task_id}")
async def delete_note(task_id):
   pass