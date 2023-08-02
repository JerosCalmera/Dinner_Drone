"""empty message

Revision ID: e64c0ceedc8c
Revises: d68b2186f7db
Create Date: 2023-08-02 14:21:07.210247

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e64c0ceedc8c'
down_revision = 'd68b2186f7db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('customers', schema=None) as batch_op:
        batch_op.alter_column('total_spend',
               existing_type=sa.NUMERIC(precision=9, scale=2),
               nullable=True)

    with op.batch_alter_table('menu', schema=None) as batch_op:
        batch_op.alter_column('item_price',
               existing_type=sa.NUMERIC(precision=9, scale=2),
               nullable=True)
        batch_op.alter_column('item_weight',
               existing_type=sa.NUMERIC(precision=9, scale=0),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('menu', schema=None) as batch_op:
        batch_op.alter_column('item_weight',
               existing_type=sa.NUMERIC(precision=9, scale=0),
               nullable=False)
        batch_op.alter_column('item_price',
               existing_type=sa.NUMERIC(precision=9, scale=2),
               nullable=False)

    with op.batch_alter_table('customers', schema=None) as batch_op:
        batch_op.alter_column('total_spend',
               existing_type=sa.NUMERIC(precision=9, scale=2),
               nullable=False)

    # ### end Alembic commands ###