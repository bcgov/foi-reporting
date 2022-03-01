"""viw_cfrrfdreport

Revision ID: 3a721e154671
Revises: 5397f07013f3
Create Date: 2022-02-28 20:05:02.089352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a721e154671'
down_revision = '5397f07013f3'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE OR REPLACE VIEW public.viw_cfrrfdreport AS SELECT r.visualrequestfilenumber AS "Request ID", rd.redactiondescription AS "Request Description", rfd.createddate AS "Request Start Date", eco2.officedescription AS "Office of Primary Interest", rfd.completeddate AS "Completed Date", rfds.reqfordocstatus AS "RFD Status", rd.status AS "Request Status", rd.primaryusername AS "Primary User", rfd.requestdescription AS "RFD Comments", rfd.rfdage AS "RFD Age", rd.requestage AS "Request Age", rfd.duedate AS "Due Date", rfd.createddate AS "Requested Date", rfd.remainingdays AS "Remaining Days", rfd.elapseddays AS "Processed Days", rt.requesttypename AS "Request Type", eco.officedescription AS "Office Name", eco.officecode AS "Office Code" FROM "factRequestForDocuments" rfd LEFT JOIN "dimRequests" r ON rfd.foirequestid = r.foirequestid LEFT JOIN "factRequestDetails" rd ON r.foirequestid = rd.foirequestid and rd.activeflag = \'Y\' LEFT JOIN "dimRequestForDocumentsStatus" rfds ON rfd.reqfordocstatusid = rfds.reqfordocstatusid LEFT JOIN "dimRequestTypes" rt ON rt.requesttypeid = rfd.requesttypeid LEFT JOIN "dimECOffice" eco ON eco.officeid = rfd.officeid LEFT JOIN "dimECOffice" eco2 ON eco2.officeid = rfd.programofficeid WHERE rfd.activeflag = \'Y\'; commit;')


def downgrade():
    op.drop_view(viw_cfrrfdreport)
