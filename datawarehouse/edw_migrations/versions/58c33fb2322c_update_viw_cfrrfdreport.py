"""update_viw_cfrrfdreport

Revision ID: 58c33fb2322c
Revises: b6a8f2338f16
Create Date: 2022-03-17 14:50:05.897051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58c33fb2322c'
down_revision = 'b6a8f2338f16'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('DROP VIEW public.viw_cfrrfdreport; CREATE OR REPLACE VIEW public.viw_cfrrfdreport AS SELECT r.visualrequestfilenumber AS "Request ID",    rd.redactiondescription AS "Request Description",    rfd.createddate AS "Request Start Date",    eco2.officedescription AS "Office of Primary Interest",    rfd.completeddate AS "Completed Date",    rfds.reqfordocstatus AS "RFD Status",    rd.status AS "Request Status",    rd.primaryusername AS "Primary User",    rfd.requestdescription AS "RFD Comments",    frfdcf.rfdage AS "RFD Age",    rd.requestage AS "Request Age",    rfd.duedate AS "Due Date",    rfd.createddate AS "Requested Date",    frfdcf.remainingdays AS "Remaining Days",    frfdcf.elapseddays AS "Processed Days",    rt.requesttypename AS "Request Type",    eco.officedescription AS "Office Name",    eco.officecode AS "Office Code"   FROM "factRequestForDocuments" rfd     LEFT JOIN "dimRequests" r ON rfd.foirequestid = r.foirequestid     LEFT JOIN "factRequestDetails" rd ON r.foirequestid = rd.foirequestid AND rd.activeflag = \'Y\'::bpchar     LEFT JOIN "dimRequestForDocumentsStatus" rfds ON rfd.reqfordocstatusid = rfds.reqfordocstatusid     LEFT JOIN "dimRequestTypes" rt ON rt.requesttypeid = rfd.requesttypeid     LEFT JOIN "dimECOffice" eco ON eco.officeid = rfd.officeid     LEFT JOIN "dimECOffice" eco2 ON eco2.officeid = rfd.programofficeid 	 LEFT JOIN "factRequestRFDCalculatedFields" frfdcf ON rfd.foirequestid = frfdcf.foirequestid and rfd.actionid = frfdcf.actionid  WHERE rfd.activeflag = \'Y\'::bpchar;ALTER TABLE public.viw_cfrrfdreport    OWNER TO postgres;GRANT ALL ON TABLE public.viw_cfrrfdreport TO postgres;GRANT SELECT ON TABLE public.viw_cfrrfdreport TO redash_role;')


def downgrade():
    op.execute('DROP VIEW public.viw_cfrrfdreport; CREATE OR REPLACE VIEW public.viw_cfrrfdreport AS SELECT r.visualrequestfilenumber AS "Request ID",    rd.redactiondescription AS "Request Description",    rfd.createddate AS "Request Start Date",    eco2.officedescription AS "Office of Primary Interest",    rfd.completeddate AS "Completed Date",    rfds.reqfordocstatus AS "RFD Status",    rd.status AS "Request Status",    rd.primaryusername AS "Primary User",    rfd.requestdescription AS "RFD Comments",    frfdcf.rfdage AS "RFD Age",    rd.requestage AS "Request Age",    rfd.duedate AS "Due Date",    rfd.createddate AS "Requested Date",    frfdcf.remainingdays AS "Remaining Days",    frfdcf.elapseddays AS "Processed Days",    rt.requesttypename AS "Request Type",    eco.officedescription AS "Office Name",    eco.officecode AS "Office Code"   FROM "factRequestForDocuments" rfd     LEFT JOIN "dimRequests" r ON rfd.foirequestid = r.foirequestid     LEFT JOIN "factRequestDetails" rd ON r.foirequestid = rd.foirequestid AND rd.activeflag = \'Y\'::bpchar     LEFT JOIN "dimRequestForDocumentsStatus" rfds ON rfd.reqfordocstatusid = rfds.reqfordocstatusid     LEFT JOIN "dimRequestTypes" rt ON rt.requesttypeid = rfd.requesttypeid     LEFT JOIN "dimECOffice" eco ON eco.officeid = rfd.officeid     LEFT JOIN "dimECOffice" eco2 ON eco2.officeid = rfd.programofficeid 	 LEFT JOIN "factRequestRFDCalculatedFields" frfdcf ON rfd.foirequestid = frfdcf.foirequestid and rfd.actionid = frfdcf.actionid  WHERE rfd.activeflag = \'Y\'::bpchar;ALTER TABLE public.viw_cfrrfdreport    OWNER TO postgres;GRANT ALL ON TABLE public.viw_cfrrfdreport TO postgres;GRANT SELECT ON TABLE public.viw_cfrrfdreport TO redash_role;')
