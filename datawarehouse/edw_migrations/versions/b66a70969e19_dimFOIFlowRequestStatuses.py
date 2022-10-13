"""empty message

Revision ID: b66a70969e19
Revises: 212cf13b0b03
Create Date: 2022-07-12 14:52:18.323116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b66a70969e19'
down_revision = '212cf13b0b03'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimFOIFlowRequestStatus',
		sa.Column('requeststatusid', sa.Integer(), nullable=False),		
		sa.Column('name', sa.VARCHAR(length=100)),
		sa.Column('description', sa.VARCHAR(255)),
        sa.Column('isactive', sa.Boolean()),		
		sa.PrimaryKeyConstraint('requeststatusid')
      )


def downgrade():
    op.drop_table('dimFOIFlowRequestStatus')
