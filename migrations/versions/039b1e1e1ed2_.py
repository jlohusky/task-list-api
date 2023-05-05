"""empty message

Revision ID: 039b1e1e1ed2
Revises: 79ac7c5f8a00
Create Date: 2023-05-04 13:15:15.867981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '039b1e1e1ed2'
down_revision = '79ac7c5f8a00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'is_complete')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('is_complete', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###