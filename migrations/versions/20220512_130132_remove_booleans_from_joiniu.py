"""remove booleans from JoinIU

Revision ID: 11f052d0a5d4
Revises: d684a56d9242
Create Date: 2022-05-12 13:01:32.613347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11f052d0a5d4'
down_revision = 'd684a56d9242'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('JoinIU', 'is_submitter')
    op.drop_column('JoinIU', 'is_assignee')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('JoinIU', sa.Column('is_assignee', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column('JoinIU', sa.Column('is_submitter', sa.BOOLEAN(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
