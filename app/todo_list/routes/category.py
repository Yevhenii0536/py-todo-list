from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.todo_list.schemas.todo_category import TodoCategoryRead, TodoCategoryCreate, TodoCategoryUpdate
from app.db.engine import get_db
from app.todo_list.crud import (
    create_category_db,
    read_category_db,
    update_category_db,
    delete_category_db,
)

from typing import List


router = APIRouter()

category_url = "/todo/category"


@router.post(category_url, response_model=TodoCategoryRead)
async def create_category(category: TodoCategoryCreate, db: AsyncSession = Depends(get_db)):
    return await create_category_db(db=db, category=category)


@router.patch(category_url, response_model=TodoCategoryRead)
async def update_category(category: TodoCategoryUpdate, db: AsyncSession = Depends(get_db)):
    return await update_category_db(db=db, category=category)


@router.get(category_url, response_model=List[TodoCategoryRead])
async def get_category(db: AsyncSession = Depends(get_db)):
    return await read_category_db(db=db)


@router.delete(category_url, response_model=dict)
async def delete_category(category_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_category_db(db=db, category_id=category_id)
