"""add content column to posts table

Revision ID: f9846e35f1c3
Revises: 5229844c26d4
Create Date: 2022-04-11 18:02:56.439723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9846e35f1c3'
down_revision = '5229844c26d4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
