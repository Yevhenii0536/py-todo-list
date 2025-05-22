from enum import StrEnum, auto
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Enum, ForeignKey, DateTime, func, Text, Index
from datetime import datetime

from app.db.engine import Base


class TodoPriority(StrEnum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


class TodoCategory(Base):
    __tablename__ = "todo_category"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), insert_default=func.now())
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, default=None, onupdate=func.now())

    todo: Mapped[list["Todo"]] = relationship("Todo", back_populates="category", cascade="all, delete-orphan")


class Todo(Base):
    __tablename__ = "todo"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), insert_default=func.now())
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, default=None, onupdate=func.now())

    priority: Mapped[TodoPriority] = mapped_column(
        Enum(TodoPriority),
        nullable=False,
        default=TodoPriority.LOW
    )
    
    category_id: Mapped[int] = mapped_column(
        ForeignKey("todo_category.id", name="fk_todo_category_id", ondelete="CASCADE"),
        nullable=False
    )

    category: Mapped["TodoCategory"] = relationship("TodoCategory", back_populates="todo", lazy="selectin")

Index('ix_todo_category_id', Todo.category_id)

