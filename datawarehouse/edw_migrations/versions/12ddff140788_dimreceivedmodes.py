"""dimReceivedModes

Revision ID: 12ddff140788
Revises: 4d95cc41347e
Create Date: 2022-01-26 23:18:35.900890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12ddff140788'
down_revision = '4d95cc41347e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimReceivedModes',
		sa.Column('receivedmodeid', sa.Integer(), nullable=False),
		sa.Column('receivedmodename', sa.VARCHAR(length=3000)),
		sa.Column('cactive', sa.CHAR(length=1)),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifieddate', sa.DateTime()),
		sa.Column('cdelete', sa.CHAR(length=1)),
		sa.PrimaryKeyConstraint('receivedmodeid')
    )


def downgrade():
    op.drop_table('dimReceivedModes')
