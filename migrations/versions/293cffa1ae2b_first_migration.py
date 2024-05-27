"""first migration

Revision ID: 293cffa1ae2b
Revises: 
Create Date: 2024-05-27 00:14:23.381145

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '293cffa1ae2b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sensor', schema=None) as batch_op:
        batch_op.alter_column('value',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.Integer(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sensor', schema=None) as batch_op:
        batch_op.alter_column('value',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)

    # ### end Alembic commands ###
