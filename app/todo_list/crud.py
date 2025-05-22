from fastapi import Depends

from app.db.engine import get_db

from sqlalchemy import select

from sqlalchemy.orm import selectinload

from app.todo_list.models import Todo

from sqlalchemy.ext.asyncio import AsyncSession

from app.todo_list.schemas.todo import TodoCreate


async def create_todo_db(db: AsyncSession, todo: TodoCreate):
    todo_db = Todo(**todo.model_dump())

    db.add(todo_db)

    await db.commit()
    await db.refresh(todo_db)

    return todo_db


async def read_todo_db(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Todo).options(selectinload(Todo.category)))

    todos = result.scalars().all()

    return todos
