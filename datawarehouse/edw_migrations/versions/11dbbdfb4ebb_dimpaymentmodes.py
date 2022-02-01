"""dimPaymentModes

Revision ID: 11dbbdfb4ebb
Revises: fa86e0a1ce0a
Create Date: 2022-01-27 00:46:43.874015

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11dbbdfb4ebb'
down_revision = 'fa86e0a1ce0a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimPaymentModes',
		sa.Column('paymentmodeid', sa.Integer(), nullable=False),
		sa.Column('paymentmodename', sa.VARCHAR(length=3000)),
		sa.Column('cactive', sa.CHAR(length=1)),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifieddate', sa.DateTime()),
		sa.Column('cdelete', sa.CHAR(length=1)),
		sa.Column('cpal', sa.CHAR(length=1)),
		sa.PrimaryKeyConstraint('paymentmodeid')
    )


def downgrade():
    op.drop_table('dimPaymentModes')
