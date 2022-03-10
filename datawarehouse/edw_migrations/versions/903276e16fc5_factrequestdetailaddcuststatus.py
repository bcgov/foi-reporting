"""factrequestdetailaddcuststatus

Revision ID: 903276e16fc5
Revises: d53acaf848c6
Create Date: 2022-03-09 17:06:48.450183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '903276e16fc5'
down_revision = 'd53acaf848c6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('factRequestDetails', sa.Column('customfieldstatus', sa.VARCHAR(length=1000)))


def downgrade():
    op.add_column('factRequestDetails', sa.Column('customfieldstatus', sa.VARCHAR(length=1000)))
