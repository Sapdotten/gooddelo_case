from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from app.routers.limiter import limiter
from app.routers.models import task_models
from app.database.managers import task_manager
from app.utils.tokens import TokenManager

router = APIRouter(
    prefix="/tasks",
    tags=["Записи"],
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/", response_model=task_models.AddTaskSuccesResponse)
@limiter.limit("100/minute")
async def create_task(
    request: Request,
    task_data: task_models.AddTaskRequest,
    token: str = Depends(oauth2_scheme),
):
    payload = TokenManager.decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid access token")
    user_id = payload["user_id"]
    try:
        task_id = await task_manager.add_new_task(user_id, task_data.task_text)
        return task_models.AddTaskSuccesResponse(
            status="succes", message="Note was succesfully added", task_id=task_id
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/", response_model=task_models.GetAllTasksSuccesResponse)
@limiter.limit("100/minute")
async def get_all_tasks(request: Request, token: str = Depends(oauth2_scheme)):
    payload = TokenManager.decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid access token")
    user_id = payload["user_id"]
    try:
        tasks = await task_manager.get_all_tasks(user_id)
        return task_models.GetAllTasksSuccesResponse(
            status="success", message="Tasks of user were found", tasks=tasks
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{task_id}", response_model=task_models.GetTaskSuccessResponse)
@limiter.limit("100/minute")
async def get_task(task_id: int, request: Request, token: str = Depends(oauth2_scheme)):
    payload = TokenManager.decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid access token")
    user_id = payload["user_id"]
    try:
        task = await task_manager.get_task(user_id, task_id)
        if task:
            return task_models.GetTaskSuccessResponse(task_text=task)
        else:
            raise HTTPException(
                status_code=404,
                detail="Task was not found or this is task of another user",
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{task_id}", response_model=task_models.EditTaskSuccessResponse)
@limiter.limit("100/minute")
async def edit_note(
    task_id: int,
    request: Request,
    task_data: task_models.EditTaskRequest,
    token: str = Depends(oauth2_scheme),
):
    payload = TokenManager.decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid access token")

    user_id = payload["user_id"]
    try:
        task = await task_manager.edit_task(user_id, task_id, task_data.task_text)
        if task:
            return task_models.EditTaskSuccessResponse(
                status="success", message="Task was edited successfuly"
            )
        else:
            raise HTTPException(
                status_code=404,
                detail="Task was not found or this is task of another user",
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{task_id}", response_model=task_models.DeleteTaskSuccessResponse)
@limiter.limit("100/minute")
async def delete_note(
    task_id: int, request: Request, token: str = Depends(oauth2_scheme)
):
    payload = TokenManager.decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid access token")

    user_id = payload["user_id"]
    try:
        task = await task_manager.delete_task(user_id, task_id)
        if task:
            return task_models.DeleteTaskSuccessResponse(
                status="success", message="Task was deleted successfuly"
            )
        else:
            raise HTTPException(
                status_code=404,
                detail="Task was not found or this is task of another user",
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
