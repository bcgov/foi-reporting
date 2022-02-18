"""dimRequestsdropcolumns

Revision ID: 7b2becd919ff
Revises: e088c426883f
Create Date: 2022-02-16 16:42:31.966311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b2becd919ff'
down_revision = 'e088c426883f'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('dimRequests', 'requestdescription')
    op.drop_column('dimRequests', 'priority')
    op.drop_column('dimRequests', 'requesterid')
    op.drop_column('dimRequests', 'onbehalfofrequesterid')
    op.drop_column('dimRequests', 'referencenumber')
    op.drop_column('dimRequests', 'refvisualrequestfilenumber')


def downgrade():
    op.drop_column('dimRequests', 'requestdescription')
    op.drop_column('dimRequests', 'priority')
    op.drop_column('dimRequests', 'requesterid')
    op.drop_column('dimRequests', 'onbehalfofrequesterid')
    op.drop_column('dimRequests', 'referencenumber')
    op.drop_column('dimRequests', 'refvisualrequestfilenumber')