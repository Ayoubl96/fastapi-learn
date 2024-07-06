"""create post table

Revision ID: 7a1600cfd8bd
Revises: d790919fe922
Create Date: 2024-07-04 23:11:34.454582

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a1600cfd8bd'
down_revision: Union[str, None] = 'd790919fe922'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('Users', sa.Column('test', sa.String(), nullable=True))
    pass


def downgrade() -> None:
    op.drop_column('Users', 'test')
    pass
