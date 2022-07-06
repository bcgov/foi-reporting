"""empty message

Revision ID: 816b50797367
Revises: 284a928c4bfd
Create Date: 2022-07-05 15:47:31.178079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '816b50797367'
down_revision = '284a928c4bfd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('dimDivisions', sa.Column('programarea', sa.VARCHAR(length=25)))


def downgrade():
    op.drop_column('dimDivisions', 'programarea')
