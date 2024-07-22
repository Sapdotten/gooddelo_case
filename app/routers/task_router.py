
from fastapi import APIRouter, Request
from app.routers.limiter import limiter
router = APIRouter(
   prefix="/tasks",
   tags=["Записи"],
)



@router.post("/")
@limiter.limit("100/minute")
async def create_note(request: Request):
   pass

@router.get("/")
@limiter.limit("100/minute")
async def get_all_notes(request: Request):
   pass

@router.get("/{task_id}")
@limiter.limit("100/minute")
async def get_note(task_id, request: Request):
   pass

@router.put("/{task_id}")
@limiter.limit("100/minute")
async def edit_note(task_id, request: Request):
   pass

@router.delete("/{task_id}")
@limiter.limit("100/minute")
async def delete_note(task_id, request: Request):
   pass