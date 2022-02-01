"""factRequestInvoices

Revision ID: 826627900ca5
Revises: 41cf021e9790
Create Date: 2022-01-28 00:50:11.240474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '826627900ca5'
down_revision = '41cf021e9790'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('factRequestInvoices',
		sa.Column('foirequestid', sa.Integer(), nullable=False),
		sa.Column('runcycleid', sa.Integer(), nullable=False),
		sa.Column('invoiceid', sa.Integer(), nullable=False),
		sa.Column('invoicenumber', sa.CHAR(length=11)),
		sa.Column('createdby', sa.Integer()),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifiedby', sa.Integer()),
		sa.Column('modifieddate', sa.DateTime()),
		sa.Column('comments', sa.VARCHAR(length=4000)),
		sa.Column('correspondenceid', sa.Integer()),
		sa.Column('invoiceamount', sa.Numeric(precision=11, scale=2)),
		sa.Column('chargedamount', sa.Numeric(precision=11, scale=2)),
		sa.Column('incurredamount', sa.Numeric(precision=11, scale=2)),
		sa.Column('feewaived', sa.Numeric(precision=11, scale=2)),
		sa.Column('admincostpercentage', sa.Numeric(precision=11, scale=2)),
		sa.Column('chargedadmincostamount', sa.Numeric(precision=11, scale=2)),
		sa.Column('incurredadmincostamount', sa.Numeric(precision=11, scale=2)),
		sa.Column('feewaivedadmincost', sa.Numeric(precision=11, scale=2)),
		sa.Column('annotationtext', sa.VARCHAR(length=4000)),
		sa.Column('invoiceddate', sa.DateTime()),
		sa.Column('approvalstatus', sa.CHAR(length=1)),
		sa.Column('approvedby', sa.Integer()),
		sa.Column('approveddate', sa.DateTime()),
		sa.ForeignKeyConstraint(['runcycleid'], ['dimRunCycle.runcycleid']),
		sa.ForeignKeyConstraint(['foirequestid'], ['dimRequests.foirequestid']),
		sa.PrimaryKeyConstraint('invoiceid','runcycleid')
    )


def downgrade():
    op.drop_table('factRequestInvoices')
