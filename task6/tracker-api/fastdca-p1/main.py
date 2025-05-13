from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr, validator
from typing import Optional, List, Annotated
from datetime import date

app = FastAPI()

# ---- Models ----

class UserCreate(BaseModel):
    username: Annotated[str, constr(min_length=3, max_length=20)]
    email: EmailStr

class UserRead(UserCreate):
    id: int

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    due_date: date
    status: str
    user_id: int

    @validator("due_date")
    def check_due_date(cls, value: date) -> date:
        if value < date.today():
            raise ValueError("Due date cannot be in the past")
        return value

    @validator("status")
    def check_status(cls, value: str) -> str:
        allowed = {"pending", "in_progress", "completed"}
        if value not in allowed:
            raise ValueError(f"Status must be one of {allowed}")
        return value

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: date
    user_id: int

    @validator("due_date")
    def check_due_date(cls, value: date) -> date:
        if value < date.today():
            raise ValueError("Due date cannot be in the past")
        return value

class TaskStatusUpdate(BaseModel):
    status: str

    @validator("status")
    def check_status(cls, value: str) -> str:
        allowed = {"pending", "in_progress", "completed"}
        if value not in allowed:
            raise ValueError(f"Status must be one of {allowed}")
        return value

# ---- In-Memory Storage ----
USERS: dict[int, UserRead] = {}
TASKS: dict[int, Task] = {}

user_id_counter = 1
task_id_counter = 1

# ---- Endpoints ----

@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    global user_id_counter
    new_user = UserRead(id=user_id_counter, **user.dict())
    USERS[user_id_counter] = new_user
    user_id_counter += 1
    return new_user

@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    global task_id_counter
    if task.user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    new_task = Task(id=task_id_counter, status="pending", **task.dict())
    TASKS[task_id_counter] = new_task
    task_id_counter += 1
    return new_task

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task_status(task_id: int, update: TaskStatusUpdate):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.status = update.status
    TASKS[task_id] = task
    return task

@app.get("/users/{user_id}/tasks", response_model=List[Task])
def get_user_tasks(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    return [task for task in TASKS.values() if task.user_id == user_id]
