from fastapi import FastAPI
from fastapi import APIRouter

router = APIRouter(
   prefix="/tasks",
   tags=["Записи"],
)


@router.post("/")
def create_note():
   pass

@router.get("/")
def get_all_notes():
   pass

@router.get("/{task_id}")
def get_note(task_id):
   pass

@router.put("/{task_id}")
def edit_note(task_id):
   pass

@router.delete("/{task_id}")
def delete_note(task_id):
   pass