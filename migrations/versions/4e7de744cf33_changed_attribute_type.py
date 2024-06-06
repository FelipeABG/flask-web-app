"""changed attribute type

Revision ID: 4e7de744cf33
Revises: abca690df86e
Create Date: 2024-06-06 19:31:55.778388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e7de744cf33'
down_revision = 'abca690df86e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('log_actuator', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=False))
        batch_op.drop_column('value')

    with op.batch_alter_table('log_humidity', schema=None) as batch_op:
        batch_op.alter_column('value',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)

    with op.batch_alter_table('log_temperature', schema=None) as batch_op:
        batch_op.alter_column('value',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('log_temperature', schema=None) as batch_op:
        batch_op.alter_column('value',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False)

    with op.batch_alter_table('log_humidity', schema=None) as batch_op:
        batch_op.alter_column('value',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False)

    with op.batch_alter_table('log_actuator', schema=None) as batch_op:
        batch_op.add_column(sa.Column('value', sa.INTEGER(), nullable=False))
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###
