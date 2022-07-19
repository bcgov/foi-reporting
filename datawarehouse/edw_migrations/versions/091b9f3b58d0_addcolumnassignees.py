"""empty message

Revision ID: 091b9f3b58d0
Revises: b66a70969e19
Create Date: 2022-07-19 11:27:52.921633

"""
from typing import Text
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '091b9f3b58d0'
down_revision = 'b66a70969e19'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('factFOIFlowRequestStatusDetails', sa.Column('iaoassignedto', sa.VARCHAR(length=250)))
    op.add_column('factFOIFlowRequestStatusDetails', sa.Column('iaoassigneefullname', sa.VARCHAR(length=700)))
    op.add_column('factFOIFlowRequestStatusDetails', sa.Column('ministryassigneefullname', sa.VARCHAR(length=700)))
    

def downgrade():
    op.drop_column('factFOIFlowRequestStatusDetails', 'iaoassignedto')
    op.drop_column('factFOIFlowRequestStatusDetails', 'iaoassigneefullname')
    op.drop_column('factFOIFlowRequestStatusDetails', 'ministryassigneefullname')
