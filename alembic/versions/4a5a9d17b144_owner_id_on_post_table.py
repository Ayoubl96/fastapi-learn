"""owner id on post table

Revision ID: 4a5a9d17b144
Revises: 73467716e10d
Create Date: 2024-07-06 02:22:20.582458

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '4a5a9d17b144'
down_revision: Union[str, None] = '73467716e10d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(
        'post_user_fk',
        source_table='posts',
        referent_table='Users',
        local_cols=['owner_id'],
        remote_cols=['id'],
        ondelete='CASCADE'
    )
    pass


def downgrade() -> None:
    op.drop_column('post_user_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
