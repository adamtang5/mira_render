"""Issue model

Revision ID: 5ddf4f7c141f
Revises: 416a494112ab
Create Date: 2022-05-11 10:01:57.581607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ddf4f7c141f'
down_revision = '416a494112ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Statuses', ['status'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Statuses', type_='unique')
    # ### end Alembic commands ###
