"""empty message

Revision ID: cb29908c1dd5
Revises: 
Create Date: 2023-08-08 14:15:18.895413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb29908c1dd5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('member_gh')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('member_gh',
    sa.Column('name', sa.VARCHAR(length=20), nullable=True),
    sa.Column('age', sa.VARCHAR(length=20), nullable=True),
    sa.Column('tel', sa.VARCHAR(length=20), nullable=True)
    )
    op.drop_table('user')
    # ### end Alembic commands ###