"""empty message

Revision ID: 9685b0955690
Revises: 9c432198c15c
Create Date: 2020-03-05 17:07:22.736941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9685b0955690'
down_revision = '9c432198c15c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cinema_movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('c_cinema_id', sa.Integer(), nullable=True),
    sa.Column('c_movie_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['c_cinema_id'], ['cinema_user.id'], ),
    sa.ForeignKeyConstraint(['c_movie_id'], ['movie.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cinema_movie')
    # ### end Alembic commands ###
