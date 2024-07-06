"""create post user

Revision ID: c00655bf078a
Revises: 7a1600cfd8bd
Create Date: 2024-07-04 23:11:56.016825

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c00655bf078a'
down_revision: Union[str, None] = '7a1600cfd8bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    pass
