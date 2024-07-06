"""ad last column on posts table

Revision ID: 4e3b4d7030e6
Revises: 4a5a9d17b144
Create Date: 2024-07-06 02:36:14.527487

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e3b4d7030e6'
down_revision: Union[str, None] = '4a5a9d17b144'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',
                  sa.Column(
                      'create_at',
                      sa.TIMESTAMP(timezone=True),
                      nullable=False,
                      server_default=sa.text('NOW()')
                )
                )
    op.add_column('posts',
                  sa.Column(
                      'published',
                      sa.Integer(),
                      nullable=False,
                      server_default=sa.text('0')
                  )
                  )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'create_at')
    pass
