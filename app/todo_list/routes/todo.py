from fastapi.routing import APIRouter
from fastapi import Depends, HTTPException, status

from app.db.engine import get_db
from app.todo_list.schemas.todo import TodoRead, TodoCreate, TodoUpdate
from app.todo_list.crud import read_todo_db, create_todo_db, delete_todo_db, update_todo_db

from sqlalchemy.ext.asyncio import AsyncSession

from typing import List


router = APIRouter()

todo_url = "/todo"

@router.post(todo_url, response_model=TodoRead)
async def create_todo(todo: TodoCreate, db: AsyncSession = Depends(get_db)):
    return await create_todo_db(todo=todo, db=db)


@router.patch(todo_url, response_model=TodoRead)
async def update_todo(todo: TodoUpdate, db: AsyncSession = Depends(get_db)):
    return await update_todo_db(todo=todo, db=db)


@router.get(todo_url, response_model=List[TodoRead])
async def read_todo(db: AsyncSession = Depends(get_db)):
    try:
        return await read_todo_db(db=db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}")


@router.delete(todo_url, response_model=dict)
async def delete_todo(todo_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_todo_db(todo_id=todo_id, db=db)
