"""dimRequestStatuses

Revision ID: 4d95cc41347e
Revises: 101cfb715b9a
Create Date: 2022-01-26 23:13:36.503723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d95cc41347e'
down_revision = '101cfb715b9a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimRequestStatuses',
		sa.Column('requeststatusid', sa.Integer(), nullable=False),
		sa.Column('requeststatusname', sa.VARCHAR(length=3000)),
		sa.Column('requeststatus', sa.VARCHAR(length=10)),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifieddate', sa.DateTime()),
		sa.PrimaryKeyConstraint('requeststatusid')
    )


def downgrade():
    op.drop_table('dimRequestStatuses')
