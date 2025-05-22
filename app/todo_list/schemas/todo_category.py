from pydantic import BaseModel, ConfigDict

from datetime import datetime

from typing import Optional


class TodoCategoryBase(BaseModel):
    title: str

    model_config = ConfigDict(from_attributes=True)


class TodoCategoryCreate(TodoCategoryBase):
    pass


class TodoCategoryUpdate(TodoCategoryCreate):
    id: int


class TodoCategoryRead(TodoCategoryBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class TodoCategoryShort(TodoCategoryBase):
    id: int