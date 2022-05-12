"""Invites join

Revision ID: a1ad532ffaa7
Revises: aef092f7e557
Create Date: 2022-05-11 11:41:31.984515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1ad532ffaa7'
down_revision = 'aef092f7e557'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Invites',
    sa.Column('issue_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['issue_id'], ['Issues.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('issue_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Invites')
    # ### end Alembic commands ###