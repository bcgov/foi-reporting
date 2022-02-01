"""factRequestExtensions

Revision ID: 0d832d32eb74
Revises: 243b2aa7349a
Create Date: 2022-01-26 18:20:11.728564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d832d32eb74'
down_revision = '243b2aa7349a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('factRequestExtensions',
		sa.Column('foirequestid', sa.Integer(), nullable=False),
		sa.Column('runcycleid', sa.Integer(), nullable=False),
		sa.Column('createdby', sa.Integer()),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifiedby', sa.Integer()),
		sa.Column('modifieddate', sa.DateTime()),
		sa.Column('cstatus', sa.CHAR(length=1)),
		sa.Column('extensiontypeid', sa.Integer()),
		sa.Column('approvedby', sa.Integer()),
		sa.Column('approveddate', sa.DateTime()),
		sa.Column('extensiondays', sa.Integer()),
		sa.Column('extendeddate', sa.DateTime()),
		sa.Column('comments', sa.VARCHAR(length=1000)),
		sa.Column('approvedcomments', sa.VARCHAR(length=1000)),
		sa.Column('requesteddays', sa.Integer()),
		sa.Column('type', sa.VARCHAR(length=200)),
		sa.Column('cnoticetooic', sa.CHAR(length=1)),
		sa.Column('completeddate', sa.DateTime()),
		sa.Column('completedby', sa.Integer()),
		sa.Column('completedcomments', sa.VARCHAR(length=1000)),
		sa.Column('ticategory', sa.Integer()),
		sa.Column('extensionactiondate', sa.DateTime()),
		sa.Column('approvedstatus', sa.CHAR(length=1)),
		sa.Column('oldtargetdate', sa.DateTime()),
		sa.Column('oldestimateddeliverydate', sa.DateTime()),
		sa.Column('consultationtype', sa.CHAR(length=1)),
		sa.Column('noofpagesdisclosed', sa.Integer()),
		sa.Column('noofpagessent', sa.Integer()),
		sa.ForeignKeyConstraint(['extensiontypeid'], ['dimExtensionTypes.extensiontypeid']),
		sa.PrimaryKeyConstraint('foirequestid', 'runcycleid')
    )


def downgrade():
    op.drop_table('factRequestExtensions')
