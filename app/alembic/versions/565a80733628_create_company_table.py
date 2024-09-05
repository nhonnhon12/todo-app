"""Create Company Table

Revision ID: 565a80733628
Revises: 
Create Date: 2024-09-05 00:26:36.591059

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from entities.company import CompanyMode

# revision identifiers, used by Alembic.
revision: str = '565a80733628'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'companies',
        sa.Column('id', sa.UUID, nullable=False, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=False),
        sa.Column('mode', sa.Enum(CompanyMode), nullable=False, default=CompanyMode.MODE_1),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime)
    )


def downgrade() -> None:
    op.drop_table('companies')
    op.execute("DROP TYPE CompanyMode;")
