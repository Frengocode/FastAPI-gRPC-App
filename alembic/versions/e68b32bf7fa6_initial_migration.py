"""Initial migration

Revision ID: e68b32bf7fa6
Revises: baf1a1d80610
Create Date: 2024-11-26 00:46:23.669244

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e68b32bf7fa6"
down_revision: Union[str, None] = "baf1a1d80610"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Создание таблицы todos
    op.create_table(
        "todos",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("date_pub", sa.TIMESTAMP(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("completed", sa.Boolean(), nullable=False, default=False),
        sa.Column("day", sa.Integer(), nullable=False, default=0),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    # Удаление таблицы todos
    op.drop_table("todos")
