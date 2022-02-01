"""factRequestPaymentTransaction

Revision ID: 4e6e81886c50
Revises: e735622f49aa
Create Date: 2022-01-27 12:07:02.559705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e6e81886c50'
down_revision = 'e735622f49aa'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('factRequestPaymentTransaction',
		sa.Column('foirequestid', sa.Integer(), nullable=False),
		sa.Column('runcycleid', sa.Integer(), nullable=False),
		sa.Column('paymentmodeid', sa.Integer()),
		sa.Column('estimatedamount', sa.Numeric(precision=11, scale=2)),
		sa.Column('incurredamount', sa.Numeric(precision=11, scale=2)),
		sa.Column('interestamount', sa.Numeric(precision=15, scale=2)),
		sa.Column('invoicenumber', sa.CHAR(length=11)),
		sa.Column('invoicedamount', sa.Numeric(precision=11, scale=2)),
		sa.Column('paidamount', sa.Numeric(precision=11, scale=2)),
		sa.Column('willingamount', sa.Numeric(precision=11, scale=2)),
		sa.Column('applicationfee', sa.Numeric(precision=11, scale=2)),
		sa.Column('applicationfeetype', sa.CHAR(length=1)),
		sa.Column('feewaivegranted', sa.CHAR(length=1)),
		sa.Column('feewaiverequested', sa.CHAR(length=1)),
		sa.Column('payallfees', sa.CHAR(length=1)),
		sa.Column('feewaivedescription', sa.VARCHAR(length=500)),
		sa.Column('invoicedate', sa.DateTime()),
		sa.Column('feewaived', sa.Numeric(precision=11, scale=2)),
		sa.Column('totalinvoicedamount', sa.Numeric(precision=38, scale=2)),
		sa.Column('prepaymentamount', sa.VARCHAR(length=20)),
		sa.Column('applicationfeeflag', sa.CHAR(length=1)),
		sa.Column('refundamount', sa.VARCHAR(length=20)),
		sa.Column('feepaidamount', sa.VARCHAR(length=20)),
		sa.Column('paymentstatus', sa.VARCHAR(length=10)),
		sa.Column('costestimated', sa.CHAR(length=1)),
		sa.ForeignKeyConstraint(['paymentmodeid'], ['dimPaymentModes.paymentmodeid']),
		sa.PrimaryKeyConstraint('foirequestid','runcycleid')
    )


def downgrade():
    op.drop_table('factRequestPaymentTransaction')