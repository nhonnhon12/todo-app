"""Create Task Table

Revision ID: c747b72921af
Revises: dfa2f30ec3c4
Create Date: 2024-09-05 16:56:18.043112

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from entities.task import TaskStatus


# revision identifiers, used by Alembic.
revision: str = 'c747b72921af'
down_revision: Union[str, None] = 'dfa2f30ec3c4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tasks',
        sa.Column('id', sa.UUID, nullable=False, primary_key=True),
        sa.Column("summary", sa.String, nullable=False),
        sa.Column("description", sa.String, nullable=False),
        sa.Column('status', sa.Enum(TaskStatus), nullable=False, default=TaskStatus.NEW),
        sa.Column('priority', sa.SmallInteger),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),
        sa.Column('user_id', sa.UUID, nullable=False)
    )
    op.create_foreign_key('fk_task_user', 'tasks', 'users', ['user_id'], ['id'])


def downgrade() -> None:
    op.drop_table('tasks')
    op.execute("DROP TYPE TaskStatus;")
