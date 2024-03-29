"""IssueType model

Revision ID: 0835392cad9f
Revises: 64f39fe2fc15
Create Date: 2022-05-10 20:49:18.297506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0835392cad9f'
down_revision = '64f39fe2fc15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('IssueTypes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('type')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('IssueTypes')
    # ### end Alembic commands ###
