"""factRequestDetails

Revision ID: fa86e0a1ce0a
Revises: 907f2e75c0e5
Create Date: 2022-01-27 00:39:45.848012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa86e0a1ce0a'
down_revision = '907f2e75c0e5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('factRequestDetails',
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
		sa.Column('receivedbyusername', sa.VARCHAR(length=150)),
		sa.Column('modifiedbyusername', sa.VARCHAR(length=150)),
		sa.Column('assignedbyid', sa.Integer()),
		sa.Column('assignedtoid', sa.Integer()),
		sa.Column('primaryusername', sa.VARCHAR(length=250)),
		sa.Column('primarygroupid', sa.Integer()),
		sa.Column('groupname', sa.VARCHAR(length=100)),
		sa.Column('officeid', sa.Integer()),
		sa.Column('ministry', sa.VARCHAR(length=1000)),
		sa.Column('subject', sa.VARCHAR(length=1000)),
		sa.Column('screeneddate', sa.DateTime()),
		sa.Column('targetdate', sa.DateTime()),
		sa.Column('amendment', sa.CHAR(length=1)),
		sa.Column('amendmentcreateddate', sa.DateTime()),
		sa.Column('amendmentcreatedby', sa.Integer()),
		sa.Column('completeddate', sa.DateTime()),
		sa.Column('completedby', sa.Integer()),
		sa.Column('deliverydate', sa.DateTime()),
		sa.Column('deliveredby', sa.Integer()),
		sa.Column('closeddate', sa.DateTime()),
		sa.Column('closedby', sa.Integer()),
		sa.Column('notes', sa.VARCHAR(length=2000)),
		sa.Column('withheldstage', sa.VARCHAR(length=10)),
		sa.Column('otheraddress', sa.VARCHAR(length=600)),
		sa.Column('holdstage', sa.VARCHAR(length=10)),
		sa.Column('holddate', sa.DateTime()),
		sa.Column('appealtype', sa.Integer()),
		sa.Column('reviewid', sa.Integer()),
		sa.Column('withhelddate', sa.DateTime()),
		sa.Column('disposition', sa.VARCHAR(length=3000)),
		sa.Column('execcomments', sa.VARCHAR(length=3100)),
		sa.Column('originaltargetdate', sa.DateTime()),
		sa.Column('redactiondescription', sa.VARCHAR(length=3000)),
		sa.Column('currentactivity', sa.VARCHAR(length=4000)),
		sa.Column('onholddays', sa.Integer()),
		sa.Column('processeddays', sa.Integer()),
		sa.Column('releaseformat', sa.VARCHAR(length=3000)),
		sa.Column('denialauthority', sa.VARCHAR(length=3000)),
		sa.Column('caseowner', sa.VARCHAR(length=150)),
		sa.Column('caseownertitle', sa.VARCHAR(length=150)),
		sa.Column('caseowneremail', sa.VARCHAR(length=255)),
		sa.Column('caseownerphone', sa.VARCHAR(length=25)),
		sa.Column('originalcloseddate', sa.DateTime()),
		sa.Column('stdduedate', sa.DateTime()),
		sa.Column('remainingdays', sa.Integer()),
		sa.Column('requestage', sa.Integer()),
		sa.Column('currentactivitydate', sa.DateTime()),
		sa.Column('crossgovtno', sa.VARCHAR(length=1000)),
		sa.Column('requestdescription', sa.VARCHAR(length=4000)),
		sa.Column('requeststatus', sa.VARCHAR(length=10)),
		sa.Column('status', sa.VARCHAR(length=100)),
		sa.Column('countontime', sa.Integer()),
		sa.Column('countoverdue', sa.Integer()),
		sa.Column('daysoverdue', sa.Integer()),
		sa.Column('publication', sa.VARCHAR(length=1000)),
		sa.Column('publicationreason', sa.VARCHAR(length=1000)),
		sa.Column('oipcno', sa.VARCHAR(length=1000)),
		sa.Column('judicialreview', sa.VARCHAR(length=1000)),
		sa.Column('reviewtype', sa.VARCHAR(length=1000)),
		sa.Column('reason', sa.VARCHAR(length=1000)),
		sa.Column('portfolioofficer', sa.VARCHAR(length=1000)),
		sa.Column('passduedays', sa.Integer()),
		sa.ForeignKeyConstraint(['requesttypeid'], ['dimRequestTypes.requesttypeid']),
		sa.ForeignKeyConstraint(['requeststatusid'], ['dimRequestStatuses.requeststatusid']),
		sa.ForeignKeyConstraint(['receivedmodeid'], ['dimReceivedModes.receivedmodeid']),
		sa.ForeignKeyConstraint(['deliverymodeid'], ['dimDeliveryModes.deliverymodeid']),
		sa.ForeignKeyConstraint(['foirequestid'], ['dimRequests.foirequestid']),
		sa.ForeignKeyConstraint(['runcycleid'], ['dimRunCycle.runcycleid']),
		sa.PrimaryKeyConstraint('runcycleid', 'foirequestid')
    )


def downgrade():
    op.drop_table('factRequestDetails')
