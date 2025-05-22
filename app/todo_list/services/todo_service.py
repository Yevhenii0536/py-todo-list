from fastapi import HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.todo_list.models import Todo


async def get_todo_by_id(todo_id: int, db: AsyncSession):
    result = await db.execute(
        select(Todo)
        .options(selectinload(Todo.category))
        .where(Todo.id == todo_id))
    
    todo_db = result.scalar_one_or_none()

    if not todo_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with ID: {todo_id} not found"
        )

    return 
