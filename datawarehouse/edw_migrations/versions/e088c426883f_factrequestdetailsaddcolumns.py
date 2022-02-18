"""factRequestDetailsaddcolumns

Revision ID: e088c426883f
Revises: f7e43a227665
Create Date: 2022-02-16 16:41:48.368495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e088c426883f'
down_revision = 'f7e43a227665'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('factRequestDetails', sa.Column('description', sa.VARCHAR(length=4000)))
    op.add_column('factRequestDetails', sa.Column('priority', sa.VARCHAR(length=3000)))
    op.add_column('factRequestDetails', sa.Column('requesterid', sa.Integer()))
    op.add_column('factRequestDetails', sa.Column('onbehalfofrequesterid', sa.Integer()))
    op.add_column('factRequestDetails', sa.Column('referencenumber', sa.Integer()))
    op.add_column('factRequestDetails', sa.Column('refvisualrequestfilenumber', sa.VARCHAR(length=50)))


def downgrade():
    op.add_column('factRequestDetails', sa.Column('description', sa.VARCHAR(length=4000)))
    op.add_column('factRequestDetails', sa.Column('priority', sa.VARCHAR(length=3000)))
    op.add_column('factRequestDetails', sa.Column('requesterid', sa.Integer()))
    op.add_column('factRequestDetails', sa.Column('onbehalfofrequesterid', sa.Integer()))
    op.add_column('factRequestDetails', sa.Column('referencenumber', sa.Integer()))
    op.add_column('factRequestDetails', sa.Column('refvisualrequestfilenumber', sa.VARCHAR(length=50)))