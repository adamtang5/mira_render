"""add column to Status model

Revision ID: 416a494112ab
Revises: b6755eaaf640
Create Date: 2022-05-11 07:32:52.099304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '416a494112ab'
down_revision = 'b6755eaaf640'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Statuses', sa.Column('description', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Statuses', 'description')
    # ### end Alembic commands ###
