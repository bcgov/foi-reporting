"""viw_sampletlreport

Revision ID: 2c804625d96a
Revises: f6baa18a740e
Create Date: 2022-02-28 20:00:57.789804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c804625d96a'
down_revision = 'f6baa18a740e'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE OR REPLACE VIEW public.viw_sampletlreport AS SELECT r.visualrequestfilenumber AS "Request ID", rt.requesttypename AS "Request Type", category.requestertypename AS "Applicant Category", rd.redactiondescription AS "Request Description", rd.startdate AS "Start Date", rd.targetdate AS "Due Date", rd.remainingdays AS "Remaining Days", rd.currentactivity AS "Current Action", rd.requeststatus AS "Request Status", rd.primaryusername AS "Primary User", rd.execcomments AS "Comments", rd.extension AS "# of Extensions Applied", lastinvoice.invoiceddate AS "Last Invoice Date", rdd.noofpagesintherequest AS "Total # of pages in a request", eco.officedescription AS "Office Name", eco.officecode AS "Office Code", rd.caseowner AS "Request Owner", (req.lastname::text || \', \'::text) || req.firstname::text AS "Applicant Name", rd.groupname AS "User Group", rd.requesteddate AS "Requested Date", rd.receiveddate AS "Received Date", rd.closeddate AS "Closed Date", rd.originalcloseddate AS "Original Closed Date", rd.requestage AS "Request Age" FROM "factRequestDetails" rd LEFT JOIN "dimRequests" r ON rd.foirequestid = r.foirequestid LEFT JOIN "dimRequestTypes" rt ON rt.requesttypeid = rd.requesttypeid LEFT JOIN "dimRequesterTypes" category ON rd.applicantcategoryid = category.requestertypeid LEFT JOIN ( SELECT DISTINCT ON ("factRequestInvoices".foirequestid) "factRequestInvoices".foirequestid, "factRequestInvoices".invoiceddate FROM "factRequestInvoices" WHERE "factRequestInvoices".activeflag = \'Y\' ORDER BY "factRequestInvoices".foirequestid, "factRequestInvoices".createddate DESC) lastinvoice ON lastinvoice.foirequestid = rd.foirequestid LEFT JOIN "factRequestDocumentsDetails" rdd ON rdd.foirequestid = rd.foirequestid and rdd.activeflag = \'Y\' LEFT JOIN "dimECOffice" eco ON eco.officeid = rd.officeid LEFT JOIN "factRequestRequesters" rr ON rd.foirequestid = rr.foirequestid and rr.activeflag = \'Y\' LEFT JOIN "dimRequesters" req ON rr.requesterid = req.requesterid WHERE rd.activeflag = \'Y\'; commit;')


def downgrade():
    op.drop_view(viw_sampletlreport)
