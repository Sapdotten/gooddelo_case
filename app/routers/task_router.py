
from fastapi import APIRouter
from routers.limiter import limiter
router = APIRouter(
   prefix="/tasks",
   tags=["Записи"],
)



@router.post("/")
@limiter.limit("100/minute")
async def create_note():
   pass

@router.get("/")
@limiter.limit("100/minute")
async def get_all_notes():
   pass

@router.get("/{task_id}")
@limiter.limit("100/minute")
async def get_note(task_id):
   pass

@router.put("/{task_id}")
@limiter.limit("100/minute")
async def edit_note(task_id):
   pass

@router.delete("/{task_id}")
@limiter.limit("100/minute")
async def delete_note(task_id):
   pass