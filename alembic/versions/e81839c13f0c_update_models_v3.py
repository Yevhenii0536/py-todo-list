"""update models v3

Revision ID: e81839c13f0c
Revises: bcc079ed09e2
Create Date: 2025-05-21 19:52:43.933604

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e81839c13f0c'
down_revision: Union[str, None] = 'bcc079ed09e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo_category',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index('ix_todo_category_id', 'todo_category', ['id'], unique=False)
    op.create_table('todo',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.Column('priority', sa.VARCHAR(length=6), nullable=False),
    sa.Column('category_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['todo_category.id'], name='fk_todo_category_id', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_todo_id', 'todo', ['id'], unique=False)
    # ### end Alembic commands ###
