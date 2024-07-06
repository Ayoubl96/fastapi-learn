"""post_votes

Revision ID: 535740bc38e3
Revises: 4e3b4d7030e6
Create Date: 2024-07-06 02:54:28.588931

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '535740bc38e3'
down_revision: Union[str, None] = '4e3b4d7030e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_votes',
                    sa.Column('post_id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('create_at_date', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'),
                              nullable=False),
                    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('post_id', 'user_id')
                    )
    op.drop_column('Users', 'test')
    op.alter_column('posts', 'published',
                    existing_type=sa.INTEGER(),
                    nullable=True,
                    existing_server_default=sa.text('0'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'published',
                    existing_type=sa.INTEGER(),
                    nullable=False,
                    existing_server_default=sa.text('0'))
    op.add_column('Users', sa.Column('test', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_table('post_votes')
    # ### end Alembic commands ###
