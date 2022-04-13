"""factRequestDetailsAddCol

Revision ID: d5ebe8047a56
Revises: beebaaca0592
Create Date: 2022-04-13 11:36:53.126744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5ebe8047a56'
down_revision = 'beebaaca0592'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('factRequestDetails', sa.Column('visualrequestfilenumber', sa.VARCHAR(length=50)))


def downgrade():
    op.drop_column('factRequestDetails', 'visualrequestfilenumber')
