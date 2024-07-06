"""add content colum post table

Revision ID: 73467716e10d
Revises: c00655bf078a
Create Date: 2024-07-04 23:27:26.265880

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '73467716e10d'
down_revision: Union[str, None] = 'c00655bf078a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
