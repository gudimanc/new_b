"""empty message

Revision ID: b31058a10365
Revises: bc26034c6c80
Create Date: 2021-09-18 02:41:17.604720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b31058a10365'
down_revision = 'bc26034c6c80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bill',
    sa.Column('bill_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('details', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('bill_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bill')
    # ### end Alembic commands ###