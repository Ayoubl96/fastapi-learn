"""ad phone number

Revision ID: 56bd1898921e
Revises: 93a7810399cf
Create Date: 2024-07-06 03:05:50.027907

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '56bd1898921e'
down_revision: Union[str, None] = '93a7810399cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
