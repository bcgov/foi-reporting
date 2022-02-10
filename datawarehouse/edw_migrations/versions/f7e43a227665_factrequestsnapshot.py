"""factRequestSnapshot

Revision ID: f7e43a227665
Revises: 886ed324665a
Create Date: 2022-01-31 12:32:33.716542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7e43a227665'
down_revision = '886ed324665a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('factRequestSnapshot',
		sa.Column('asofdate', sa.DateTime(), nullable=False),
		sa.Column('runcycleid', sa.Integer(), nullable=False),
		sa.Column('foirequestid', sa.Integer(), nullable=False),
		sa.Column('requesttypeid', sa.Integer()),
		sa.Column('requeststatusid', sa.Integer()),
		sa.Column('receivedmodeid', sa.Integer()),
		sa.Column('deliverymodeid', sa.Integer()),
		sa.Column('applicantcategoryid', sa.Integer()),
		sa.Column('requesteddate', sa.DateTime()),
		sa.Column('receiveddate', sa.DateTime()),
		sa.Column('startdate', sa.DateTime()),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifieddate', sa.DateTime()),
		sa.Column('assigneddate', sa.DateTime()),
		sa.Column('primaryusername', sa.VARCHAR(length=250)),
		sa.Column('primarygroupid', sa.Integer()),
		sa.Column('officeid', sa.Integer()),
		sa.Column('ministry', sa.VARCHAR(length=1000)),
		sa.Column('screeneddate', sa.DateTime()),
		sa.Column('targetdate', sa.DateTime()),
		sa.Column('completeddate', sa.DateTime()),
		sa.Column('deliverydate', sa.DateTime()),
		sa.Column('closeddate', sa.DateTime()),
		sa.Column('withheldstage', sa.VARCHAR(length=10)),
		sa.Column('holdstage', sa.VARCHAR(length=10)),
		sa.Column('holddate', sa.DateTime()),
		sa.Column('withhelddate', sa.DateTime()),
		sa.Column('originaltargetdate', sa.DateTime()),
		sa.Column('originalcloseddate', sa.DateTime()),
		sa.Column('caseowner', sa.VARCHAR(length=150)),
		sa.Column('caseownertitle', sa.VARCHAR(length=150)),
		sa.Column('caseowneremail', sa.VARCHAR(length=255)),
		sa.Column('caseownerphone', sa.VARCHAR(length=25)),
		sa.Column('stdduedate', sa.DateTime()),
		sa.Column('currentactivitydate', sa.DateTime()),
		sa.Column('requeststatus', sa.VARCHAR(length=10)),
		sa.Column('status', sa.VARCHAR(length=100)),
		sa.ForeignKeyConstraint(['requesttypeid'], ['dimRequestTypes.requesttypeid']),
		sa.ForeignKeyConstraint(['requeststatusid'], ['dimRequestStatuses.requeststatusid']),
		sa.ForeignKeyConstraint(['receivedmodeid'], ['dimReceivedModes.receivedmodeid']),
		sa.ForeignKeyConstraint(['deliverymodeid'], ['dimDeliveryModes.deliverymodeid']),
		sa.ForeignKeyConstraint(['foirequestid'], ['dimRequests.foirequestid']),
		sa.ForeignKeyConstraint(['runcycleid'], ['dimRunCycle.runcycleid']),
		sa.PrimaryKeyConstraint('asofdate', 'runcycleid', 'foirequestid')
    )


def downgrade():
    op.drop_table('factRequestSnapshot')
