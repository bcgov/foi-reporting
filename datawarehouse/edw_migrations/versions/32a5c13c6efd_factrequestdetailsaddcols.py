"""factRequestDetailsaddcols

Revision ID: 32a5c13c6efd
Revises: 7ba38127b650
Create Date: 2022-02-28 19:57:56.182275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32a5c13c6efd'
down_revision = '7ba38127b650'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('factRequestDetails', sa.Column('shipaddressid', sa.Integer()))
    op.add_column('factRequestDetails', sa.Column('billaddressid', sa.Integer()))
    op.add_column('factRequestDetails', sa.Column('originalreceiveddate', sa.DateTime()))
    op.add_column('factRequestDetails', sa.Column('coordinatednrresponsereqd', sa.VARCHAR(length=1000)))
    op.add_column('factRequestDetails', sa.Column('applicantfilereference', sa.VARCHAR(length=1000)))


def downgrade():
    op.add_column('factRequestDetails', sa.Column('shipaddressid', sa.Integer()))
    op.add_column('factRequestDetails', sa.Column('billaddressid', sa.Integer()))
    op.add_column('factRequestDetails', sa.Column('originalreceiveddate', sa.DateTime()))
    op.add_column('factRequestDetails', sa.Column('coordinatednrresponsereqd', sa.VARCHAR(length=1000)))
    op.add_column('factRequestDetails', sa.Column('applicantfilereference', sa.VARCHAR(length=1000)))
