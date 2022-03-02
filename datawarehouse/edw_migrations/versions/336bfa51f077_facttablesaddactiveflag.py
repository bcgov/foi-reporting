"""facttablesaddactiveflag

Revision ID: 336bfa51f077
Revises: 32a5c13c6efd
Create Date: 2022-02-28 19:58:46.104675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '336bfa51f077'
down_revision = '32a5c13c6efd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('factRequestDetails', sa.Column('secondaryusers', sa.VARCHAR(length=3000)))
    op.add_column('factRequestDetails', sa.Column('noofdocdelivered', sa.Integer()))
    op.add_column('factRequestDetails', sa.Column('activeflag', sa.CHAR(length=1)))
    op.add_column('factRequestPaymentTransaction', sa.Column('paymentreceiveddate', sa.DateTime()))
    op.add_column('factRequestPaymentTransaction', sa.Column('activeflag', sa.CHAR(length=1)))
    op.add_column('factRequestDocumentReviewLog', sa.Column('activeflag', sa.CHAR(length=1)))
    op.add_column('factRequestRedactionLayers', sa.Column('activeflag', sa.CHAR(length=1)))
    op.add_column('factRequestExtensions', sa.Column('activeflag', sa.CHAR(length=1)))
    op.add_column('factRequestDocumentsDetails', sa.Column('activeflag', sa.CHAR(length=1)))
    op.add_column('factRequestInvoices', sa.Column('activeflag', sa.CHAR(length=1)))
    op.add_column('factRequestRequesters', sa.Column('activeflag', sa.CHAR(length=1)))
    op.add_column('factRequestForDocuments', sa.Column('activeflag', sa.CHAR(length=1)))


def downgrade():
    op.add_column('factRequestDetails', sa.Column('secondaryusers', sa.VARCHAR(length=3000)))
    op.add_column('factRequestDetails', sa.Column('noofdocdelivered', sa.Integer()))
    op.add_column('factRequestDetails', sa.Column('activeflag', sa.CHAR(length=1)))
    op.add_column('factRequestPaymentTransaction', sa.Column('paymentreceiveddate', sa.DateTime()))
    op.add_column('factRequestPaymentTransaction', sa.Column('activeflag', sa.CHAR(length=1)))
    op.add_column('factRequestDocumentReviewLog', sa.Column('activeflag', sa.CHAR(length=1)))
    op.add_column('factRequestRedactionLayers', sa.Column('activeflag', sa.CHAR(length=1)))
    op.add_column('factRequestExtensions', sa.Column('activeflag', sa.CHAR(length=1)))
    op.add_column('factRequestDocumentsDetails', sa.Column('activeflag', sa.CHAR(length=1)))
    op.add_column('factRequestInvoices', sa.Column('activeflag', sa.CHAR(length=1)))
    op.add_column('factRequestRequesters', sa.Column('activeflag', sa.CHAR(length=1)))
    op.add_column('factRequestForDocuments', sa.Column('activeflag', sa.CHAR(length=1)))
