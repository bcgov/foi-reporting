"""empty message

Revision ID: 2e6cf8a26f8f
Revises: adb323f88d99
Create Date: 2022-03-25 09:58:43.174778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e6cf8a26f8f'
down_revision = 'adb323f88d99'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('DROP VIEW public.viw_additionalfields;')
    op.execute('DROP VIEW public.viw_broaderaxisfields;')
    op.alter_column('factRequestCustomCalcFields', 'linkedrequests', type_=sa.Text, existing_type=sa.VARCHAR(length=3000))
    op.alter_column('factRequestCustomCalcFields', 'secondaryusers', type_=sa.Text, existing_type=sa.VARCHAR(length=3000))
    op.execute('CREATE OR REPLACE VIEW public.viw_additionalfields AS '\
        'SELECT r.visualrequestfilenumber AS "Request ID", '\
        'frccf.identityverification,'\
        'frccf.previousfoirequest,'\
        'frccf.physicalpageestimate,'\
        'frccf.electronicpageestimate,'\
        'frccf.noofpagesdeduplicated,'\
        'frccf.applicationfeepaid,'\
        'frccf.applicationfeerefunded ,'\
        'frccf.applicationfeetransferred,'\
        'frccf.linkedrequests,'\
        'eco.officecode AS "Action Office",'\
        'rd.closeddate AS "Closed Date",'\
        'rd.targetdate AS "Due Date"'\
        ' FROM "factRequestDetails" rd '\
            'LEFT JOIN "dimRequests" r ON rd.foirequestid = r.foirequestid '\
            'LEFT JOIN "dimECOffice" eco ON rd.officeid = eco.officeid '\
            'LEFT JOIN "factRequestDocumentsDetails" rdd ON r.foirequestid = rdd.foirequestid AND rdd.activeflag = \'Y\'::bpchar '\
            
            'LEFT JOIN "factRequestCustomCalcFields" frccf ON rd.foirequestid = frccf.foirequestid '\
        ' WHERE rd.activeflag = \'Y\'::bpchar; ALTER TABLE public.viw_additionalfields    OWNER TO postgres;GRANT ALL ON TABLE public.viw_additionalfields TO postgres;GRANT SELECT ON TABLE public.viw_additionalfields TO redash_role; ')
    op.execute('CREATE OR REPLACE VIEW public.viw_broaderaxisfields AS SELECT r.visualrequestfilenumber AS "Request ID",    re.extensiondays AS "# of days extended",    frccf.noofdocdelivered AS "# of documents delivered",    frccf.noofpagesreleased AS "# of pages released",    frccf.noofpagesreviewed AS "# of pages reviewed",    eco.officecode AS "Action Office",    rd.amendmentcreateddate AS "Amended Date",    rpt.estimatedamount AS "Amount Estimated ($)",    rpt.paidamount AS "Amount Paid ($)",    (((((((((abill.address1::text || \', \'::text) || abill.address2::text) || \', \'::text) || abill.city::text) || \', \'::text) || abill.state::text) || \', \'::text) || abill.country::text) || \', \'::text) || abill.zipcode::text AS "Applicant Billing Address",    rqstrt.requestertypename AS "Applicant Category",    rqstr.email AS "Applicant Email",    rqstr.fax AS "Applicant Fax",    rpt.applicationfee AS "Application Fee ($)",    rd.refvisualrequestfilenumber AS "Applicant\'s File Reference",    rqstr.home AS "Applicant Home Phone",    rqstr.mobile AS "Applicant Mobile",    rqstr.fullname AS "Applicant Name",    (((((((((aship.address1::text || \', \'::text) || aship.address2::text) || \', \'::text) || aship.city::text) || \', \'::text) || aship.state::text) || \', \'::text) || aship.country::text) || \', \'::text) || aship.zipcode::text AS "Applicant Shipping Address",    rqstr.workphone1 AS "Applicant Work Phone1",    rqstr.workphone2 AS "Applicant Work Phone2",    rpt.invoicedamount - rpt.paidamount AS "Balance Amount ($)",    COALESCE(( SELECT sum(COALESCE(ri.chargedamount, 0::numeric)) AS sum           FROM "factRequestInvoices" ri          WHERE ri.activeflag = \'Y\'::bpchar AND rd.activeflag = \'Y\'::bpchar AND rd.foirequestid = ri.foirequestid AND ri.invoicenumber <> \'0\'::bpchar          GROUP BY ri.foirequestid), 0::numeric) AS "Charged Amount ($)",    rd.closedby AS "Closed By",    rd.closeddate AS "Closed Date",    rd.notes AS "Comments",    frccf.coordinatednrresponsereqd AS "Coordinated NR Response Req\'d",    rd.receivedbyusername AS "Created By",    rd.createddate AS "Created Date",    rd.currentactivity AS "Current Action",    rd.deliverydate AS "Delivery Date",    dm.deliverymodename AS "Delivery Mode",    rd.targetdate AS "Due Date",    re.approveddate AS "Extension Approval/Denial Date",    re.approvedcomments AS "Extension Approval/Denial Note",    re.completeddate AS "Extension Completed Date",    re.completedcomments AS "Extension Completion Note",    re.comments AS "Extension Note",    et.extensiontypename AS "Extension Reason",        CASE            WHEN re.cstatus = \'C\'::bpchar AND re.approvedstatus = \'A\'::bpchar THEN \'Completed (Approved)\'::text            WHEN re.cstatus = \'P\'::bpchar AND re.approvedstatus = \'N\'::bpchar THEN \'Pending\'::text            WHEN re.cstatus = \'A\'::bpchar AND re.approvedstatus = \'A\'::bpchar THEN \'Approved\'::text            WHEN re.cstatus = \'D\'::bpchar AND re.approvedstatus = \'D\'::bpchar THEN \'Denied\'::text            WHEN re.cstatus = \'C\'::bpchar AND re.approvedstatus = \'D\'::bpchar THEN \'Completed (Denied)\'::text            ELSE NULL::text        END AS "Extension Status",    rpt.feewaivedescription AS "Fee Waiver Request Reason",    rpt.feewaiverequested AS "Fee Waiver Requested",    rpt.feewaivegranted AS "Fee Waiver Status",    rd.disposition AS "Final Disposition",    rpt.invoicedamount AS "Last Invoice Amount ($)",    rpt.invoicedate AS "Last Invoice Date",    rpt.invoicenumber AS "Last Invoice Number",    frccf.applicantfilereference AS "Link Requests",    pm.paymentmodename AS "Method of Payment",    frccf.noofpagesdeduplicated AS "Number of Pages Deduplicated",    onbehalfofrequesterid.fullname AS "On Behalf Of",    rqstr.company AS "Organization",    rd.originalcloseddate AS "Original Closed Date",    rd.originaltargetdate AS "Original Due Date",    rd.originalreceiveddate AS "Original Start Date",    rpt.paymentreceiveddate AS "Payment Date",    rpt.paymentstatus AS "Payment Status",    rd.primaryusername AS "Primary User",    ecg.groupname AS "Primary User Group",    rd.processeddays AS "Processed Days",    rd.receiveddate AS "Received Date",    rm.receivedmodename AS "Received Mode",    rd.referencenumber AS "Reference Number",    frccf.refundamount AS "Refund Amount",    rd.remainingdays AS "Remaining Days",    rd.requestdescription AS "Request Description",    rd.caseowner AS "Request Owner",    rd.status AS "Request Status",    rt.requesttypename AS "Request Type",    frccf.secondaryusers AS "Secondary Users",    rd.startdate AS "Start Date",    frccf.subject AS "Subject",    rdd.noofpagesintherequest AS "Total # of pages in a request",    rdd.noofpagesinreviewlog AS "Total # of pages in the review log",    frccf.onholddays AS "Total Days on Hold",    rpt.totalinvoicedamount AS "Total Invoiced ($)",    frccf.crossgovtno AS "XGOV"   FROM "factRequestDetails" rd     LEFT JOIN "dimRequests" r ON rd.foirequestid = r.foirequestid     LEFT JOIN "dimECOffice" eco ON rd.officeid = eco.officeid     LEFT JOIN "dimAddress" aship ON rd.shipaddressid = aship.addressid     LEFT JOIN "dimAddress" abill ON rd.billaddressid = abill.addressid     LEFT JOIN "factRequestExtensions" re ON r.foirequestid = re.foirequestid AND re.activeflag = \'Y\'::bpchar     LEFT JOIN "dimExtensionTypes" et ON re.extensiontypeid = et.extensiontypeid     LEFT JOIN "factRequestRequesters" rr ON r.foirequestid = rr.foirequestid AND rr.activeflag = \'Y\'::bpchar     LEFT JOIN "dimRequesters" rqstr ON rr.requesterid = rqstr.requesterid     LEFT JOIN "dimReceivedModes" rm ON rd.receivedmodeid = rm.receivedmodeid     LEFT JOIN "dimDeliveryModes" dm ON rd.deliverymodeid = dm.deliverymodeid     LEFT JOIN "dimECGroups" ecg ON rd.primarygroupid = ecg.groupid     LEFT JOIN "dimRequestTypes" rt ON rd.requesttypeid = rt.requesttypeid     LEFT JOIN "factRequestDocumentsDetails" rdd ON r.foirequestid = rdd.foirequestid AND rdd.activeflag = \'Y\'::bpchar     LEFT JOIN "factRequestPaymentTransaction" rpt ON r.foirequestid = rpt.foirequestid AND rpt.activeflag = \'Y\'::bpchar     LEFT JOIN "dimPaymentModes" pm ON rpt.paymentmodeid = pm.paymentmodeid     LEFT JOIN "dimRequesters" onbehalfofrequesterid ON rd.onbehalfofrequesterid = onbehalfofrequesterid.requesterid     LEFT JOIN "dimRequesterTypes" rqstrt ON rd.applicantcategoryid = rqstrt.requestertypeid 	 LEFT JOIN public."factRequestCustomCalcFields" frccf on rd.foirequestid = frccf.foirequestid  WHERE rd.activeflag = \'Y\'::bpchar;ALTER TABLE public.viw_broaderaxisfields    OWNER TO postgres;GRANT ALL ON TABLE public.viw_broaderaxisfields TO postgres;GRANT SELECT ON TABLE public.viw_broaderaxisfields TO redash_role;		')

def downgrade():
    op.alter_column('factRequestCustomCalcFields', 'linkedrequests', type_=sa.VARCHAR(length=3000), existing_type=sa.Text)
    op.alter_column('factRequestCustomCalcFields', 'secondaryusers', type_=sa.VARCHAR(length=3000), existing_type=sa.Text)
