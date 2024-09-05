"""Create User Table

Revision ID: dfa2f30ec3c4
Revises: 565a80733628
Create Date: 2024-09-05 16:56:05.682939

"""
from uuid import uuid4
from typing import Sequence, Union

from alembic import op
from entities.user import get_password_hash
import sqlalchemy as sa
from services import utils
from settings import ADMIN_DEFAULT_PASSWORD


# revision identifiers, used by Alembic.
revision: str = 'dfa2f30ec3c4'
down_revision: Union[str, None] = '565a80733628'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    user_table = op.create_table(
        'users',
        sa.Column('id', sa.UUID, nullable=False, primary_key=True),
        sa.Column("email", sa.String, unique=True, nullable=True, index=True),
        sa.Column("username", sa.String, unique=True, index=True),
        sa.Column("first_name", sa.String, nullable=False),
        sa.Column("last_name", sa.String, nullable=False),
        sa.Column("hashed_password", sa.String, nullable=False),
        sa.Column("is_active", sa.Boolean, default=True),
        sa.Column("is_admin", sa.Boolean, default=False),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),
        sa.Column('company_id', sa.UUID, nullable=True)
    )
    op.create_index("idx_usr_fst_lst_name", "users", ["first_name", "last_name"])
    op.create_foreign_key('fk_user_company', 'users', 'companies', ['company_id'], ['id'])

    # Data seed for first user
    op.bulk_insert(user_table, [
        {
            "id": uuid4(),
            "email": "admin@sample.com", 
            "username": "admin",
            "hashed_password": get_password_hash(ADMIN_DEFAULT_PASSWORD),
            "first_name": "FastApi",
            "last_name": "Admin",
            "is_active": True,
            "is_admin": True,
            "created_at": utils.get_current_utc_time(),
            "updated_at": utils.get_current_utc_time()
        }
    ])


def downgrade() -> None:
    op.drop_table('users')
