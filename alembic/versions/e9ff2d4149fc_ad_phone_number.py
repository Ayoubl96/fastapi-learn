"""ad phone number

Revision ID: e9ff2d4149fc
Revises: 56bd1898921e
Create Date: 2024-07-06 03:06:22.294599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9ff2d4149fc'
down_revision: Union[str, None] = '56bd1898921e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass