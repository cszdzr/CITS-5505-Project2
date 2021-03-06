"""change youtube id to thumbnail url

Revision ID: 356d5ec3bf71
Revises: 1358ad741915
Create Date: 2021-05-11 16:11:40.009867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '356d5ec3bf71'
down_revision = '1358ad741915'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course', sa.Column('thumbnail', sa.String(length=128), nullable=True))
    op.drop_column('course', 'youtube_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course', sa.Column('youtube_id', sa.VARCHAR(length=128), nullable=True))
    op.drop_column('course', 'thumbnail')
    # ### end Alembic commands ###
