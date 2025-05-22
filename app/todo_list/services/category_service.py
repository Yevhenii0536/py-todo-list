from fastapi import HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.todo_list.models import TodoCategory


async def get_todo_category_by_id(category_id: int, db: AsyncSession):
    result = await db.execute(select(TodoCategory).where(TodoCategory.id == category_id))
    category_db = result.scalar_one_or_none()

    if not category_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Category with ID: {category_id} doesn't exists"
        )
    
    return category_db
