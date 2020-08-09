"""add precipitation

Revision ID: 2340420ce2e1
Revises: fe7071f629d0
Create Date: 2020-08-09 13:50:40.756530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2340420ce2e1'
down_revision = 'fe7071f629d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('forecast', sa.Column('precipitation', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('forecast', 'precipitation')
    # ### end Alembic commands ###
