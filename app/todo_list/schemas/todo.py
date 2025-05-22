from pydantic import BaseModel, ConfigDict
from typing import Optional

from app.todo_list.models import TodoPriority
from app.todo_list.schemas.todo_category import TodoCategoryShort

from datetime import datetime


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: TodoPriority

    model_config = ConfigDict(from_attributes=True)



class TodoCreate(TodoBase):
    category_id: int


class TodoRead(TodoBase):
    id: int
    category: TodoCategoryShort

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
