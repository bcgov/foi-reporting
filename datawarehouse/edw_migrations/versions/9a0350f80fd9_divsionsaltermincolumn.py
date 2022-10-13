"""empty message

Revision ID: 9a0350f80fd9
Revises: 816b50797367
Create Date: 2022-07-05 16:11:50.599922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a0350f80fd9'
down_revision = '816b50797367'
branch_labels = None
depends_on = None


def upgrade():   
    op.alter_column('dimDivisions', 'programarea', type_=sa.VARCHAR(length=30), existing_type=sa.VARCHAR(length=25))


def downgrade():
     op.alter_column('dimDivisions', 'programarea', type_=sa.VARCHAR(length=25), existing_type=sa.VARCHAR(length=30))
