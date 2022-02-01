"""dimInvoiceDetails

Revision ID: 41cf021e9790
Revises: 386a3cb76d1c
Create Date: 2022-01-28 00:49:20.250383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41cf021e9790'
down_revision = '386a3cb76d1c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimInvoiceDetails',
		sa.Column('invoiceid', sa.Integer(), nullable=False),
		sa.Column('feetypeid', sa.Integer(), nullable=False),
		sa.Column('invoiceamount', sa.Numeric(precision=11, scale=2)),
		sa.Column('unitvalue', sa.Numeric(precision=10, scale=2)),
		sa.Column('units', sa.Numeric(precision=10, scale=2)),
		sa.Column('chargedamount', sa.Numeric(precision=11, scale=2)),
		sa.Column('incurredamount', sa.Numeric(precision=11, scale=2)),
		sa.Column('feewaived', sa.Numeric(precision=11, scale=2)),
		sa.PrimaryKeyConstraint('invoiceid', 'feetypeid')
    )


def downgrade():
    op.drop_table('dimInvoiceDetails')
