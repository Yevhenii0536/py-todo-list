from fastapi import HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError

from app.todo_list.models import Todo, TodoCategory
from app.todo_list.schemas.todo import TodoCreate, TodoUpdate
from app.todo_list.schemas.todo_category import TodoCategoryCreate, TodoCategoryUpdate
from app.todo_list.services.todo_service import get_todo_by_id
from app.todo_list.services.category_service import get_todo_category_by_id


# Todo
async def create_todo_db(db: AsyncSession, todo: TodoCreate):
    await get_todo_category_by_id(category_id=todo.category_id, db=db)

    todo_db = Todo(**todo.model_dump(exclude_none=True))

    db.add(todo_db)

    await db.commit()
    await db.refresh(todo_db)

    return todo_db


async def read_todo_db(db: AsyncSession):
    result = await db.execute(select(Todo).options(selectinload(Todo.category)))
    todo_db = result.scalars().all()

    return todo_db


async def delete_todo_db(todo_id: int, db: AsyncSession):
    todo_db = await get_todo_by_id(todo_id=todo_id, db=db)
    
    await db.delete(todo_db)
    await db.commit()

    return { "status": "ok" }


async def update_todo_db(todo: TodoUpdate, db: AsyncSession):
    todo_db = await get_todo_by_id(todo_id=todo.id, db=db)

    for key, value in todo.model_dump(exclude_unset=True).items():
        setattr(todo_db, key, value)

    await db.commit()
    await db.refresh(todo_db)

    return todo_db


# Category
async def create_category_db(db: AsyncSession, category: TodoCategoryCreate):
    category_db = TodoCategory(**category.model_dump(exclude_none=True))

    db.add(category_db)

    try:
        await db.commit()
        await db.refresh(category_db)
        return category_db
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Category with title: {category.title} already exists"
        )


async def read_category_db(db: AsyncSession):
    result = await db.execute(select(TodoCategory))
    category = result.scalars().all()

    return category


async def update_category_db(db: AsyncSession, category: TodoCategoryUpdate):
    category_db = await get_todo_category_by_id(category_id=category.id, db=db)

    if category_db.title == category.title:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Category already has '{category.title}' title"
        )

    for key, value in category.model_dump(exclude_none=True).items():
        setattr(category_db, key, value)

    await db.commit()
    await db.refresh(category_db)

    return category_db


async def delete_category_db(db: AsyncSession, category_id: int):
    category_db = await get_todo_category_by_id(category_id=category_id, db=db)

    await db.delete(category_db)
    await db.commit()
    
    return { "status": "ok" }
