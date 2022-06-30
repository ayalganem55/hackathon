"""empty message

Revision ID: 991cf641ae15
Revises: d3258c92dbdf
Create Date: 2022-06-29 15:44:06.944014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '991cf641ae15'
down_revision = 'd3258c92dbdf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('card',
    sa.Column('card_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('category', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('website', sa.String(length=64), nullable=True),
    sa.Column('facebook', sa.String(length=64), nullable=True),
    sa.Column('address', sa.String(length=64), nullable=True),
    sa.Column('sentence', sa.String(length=64), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('card_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('card')
    op.drop_table('user')
    # ### end Alembic commands ###