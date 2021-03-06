"""add phone_number true

Revision ID: 9599ea256d99
Revises: 2e97d928b77a
Create Date: 2022-04-11 18:49:52.677791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9599ea256d99'
down_revision = '2e97d928b77a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
