from fastapi.routing import APIRouter
from fastapi import Depends, HTTPException, status

from app.db.engine import get_db

from app.todo_list.schemas.todo import TodoRead, TodoCreate

from sqlalchemy.ext.asyncio import AsyncSession

from typing import List

from app.todo_list.crud import read_todo_db, create_todo_db

router = APIRouter()


@router.get("/todo", response_model=List[TodoRead])
async def read_todo(db: AsyncSession = Depends(get_db)):
    try:
        return await read_todo_db(db=db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}")


@router.post("/todo", response_model=TodoRead)
async def create_todo(todo: TodoCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await create_todo_db(todo=todo, db=db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}")
