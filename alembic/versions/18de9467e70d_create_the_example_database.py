"""Create the example Database

Revision ID: 18de9467e70d
Revises: f5b7ce6c954e
Create Date: 2021-03-20 23:46:48.788670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18de9467e70d'
down_revision = 'f5b7ce6c954e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('fullname2', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'fullname2')
    # ### end Alembic commands ###