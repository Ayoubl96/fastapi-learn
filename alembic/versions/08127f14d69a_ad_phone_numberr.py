"""ad phone numberr

Revision ID: 08127f14d69a
Revises: e9ff2d4149fc
Create Date: 2024-07-06 03:06:59.244819

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08127f14d69a'
down_revision: Union[str, None] = 'e9ff2d4149fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
