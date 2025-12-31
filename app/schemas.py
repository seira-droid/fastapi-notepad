from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    class Config:
        from_attributes = True

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    due_date: Optional[datetime] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None
    due_date: Optional[datetime] = None
    owner_id: int
    class Config:
        from_attributes = True
