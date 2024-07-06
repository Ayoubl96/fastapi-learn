"""drop test column from users

Revision ID: 93a7810399cf
Revises: 535740bc38e3
Create Date: 2024-07-06 03:02:33.580643

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93a7810399cf'
down_revision: Union[str, None] = '535740bc38e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
