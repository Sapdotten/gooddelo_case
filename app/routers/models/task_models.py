from pydantic import BaseModel
from typing import List


class AddTaskRequest(BaseModel):
    task_text: str


class AddTaskSuccesResponse(BaseModel):
    status: str
    message: str
    task_id: int


class TaskModel(BaseModel):
    task_id: int
    task_text: str


class GetAllTasksSuccesResponse(BaseModel):
    status: str
    message: str
    tasks: List[TaskModel]


class GetTaskSuccessResponse(BaseModel):
    task_text: str
     
class EditTaskRequest(BaseModel):
    task_text: str
    
class EditTaskSuccessResponse(BaseModel):
    status: str
    message: str
    
class DeleteTaskSuccessResponse(BaseModel):
    status: str
    message: str