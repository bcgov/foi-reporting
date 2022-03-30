"""viw_activeoipcreviews

Revision ID: e902c9221d33
Revises: 903276e16fc5
Create Date: 2022-03-09 18:01:40.877566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e902c9221d33'
down_revision = '903276e16fc5'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE OR REPLACE VIEW public.viw_activeoipcreviews AS SELECT r.visualrequestfilenumber AS "Request ID", rd.oipcno AS "OIPC No", rd.primaryusername AS "Primary User", rd.startdate AS "Start Date", rd.targetdate AS "Due Date", rd.reviewtype AS "Review Type", rd.customfieldstatus AS "Status", rd.reason AS "Reason", rd.requestdescription AS "Request Description", rd.subject AS "Subject", rqt.requestertypename AS "Applicant Type", rd.portfolioofficer AS "Portfolio Officer", rd.judicialreview AS "Judicial Review", rd.status AS "Request Status", rs.requeststatusname AS "Request Status Name", eco.officecode AS procorg From public."factRequestDetails" rd LEFT JOIN public."dimRequests" r on rd.foirequestid = r.foirequestid LEFT JOIN public."dimRequesterTypes" rqt on rd.applicantcategoryid = rqt.requestertypeid LEFT JOIN public."dimRequestStatuses" rs on rd.requeststatusid = rs.requeststatusid LEFT JOIN "dimECOffice" eco ON rd.officeid = eco.officeid where rd.requesttypeid = (Select requesttypeid from public."dimRequestTypes" rt where requesttypename = \'Review\') and rd.activeflag = \'Y\';')


def downgrade():
    op.execute('CREATE OR REPLACE VIEW public.viw_activeoipcreviews AS SELECT r.visualrequestfilenumber AS "Request ID", rd.oipcno AS "OIPC No", rd.primaryusername AS "Primary User", rd.startdate AS "Start Date", rd.targetdate AS "Due Date", rd.reviewtype AS "Review Type", rd.customfieldstatus AS "Status", rd.reason AS "Reason", rd.requestdescription AS "Request Description", rd.subject AS "Subject", rqt.requestertypename AS "Applicant Type", rd.portfolioofficer AS "Portfolio Officer", rd.judicialreview AS "Judicial Review", rd.status AS "Request Status", rs.requeststatusname AS "Request Status Name", eco.officecode AS procorg From public."factRequestDetails" rd LEFT JOIN public."dimRequests" r on rd.foirequestid = r.foirequestid LEFT JOIN public."dimRequesterTypes" rqt on rd.applicantcategoryid = rqt.requestertypeid LEFT JOIN public."dimRequestStatuses" rs on rd.requeststatusid = rs.requeststatusid LEFT JOIN "dimECOffice" eco ON rd.officeid = eco.officeid where rd.requesttypeid = (Select requesttypeid from public."dimRequestTypes" rt where requesttypename = \'Review\') and rd.activeflag = \'Y\';')
