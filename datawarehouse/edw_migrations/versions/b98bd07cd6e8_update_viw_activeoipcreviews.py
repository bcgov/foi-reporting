"""update_viw_activeoipcreviews

Revision ID: b98bd07cd6e8
Revises: b25c9f49e1f1
Create Date: 2022-03-17 13:11:46.632925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b98bd07cd6e8'
down_revision = 'b25c9f49e1f1'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('DROP VIEW public.viw_activeoipcreviews; CREATE OR REPLACE VIEW public.viw_activeoipcreviews AS SELECT r.visualrequestfilenumber AS "Request ID", frccf.oipcno AS "OIPC No", rd.primaryusername AS "Primary User", rd.startdate AS "Start Date", rd.targetdate AS "Due Date", frccf.reviewtype AS "Review Type",     frccf.customfieldstatus AS "Status",     frccf.reason AS "Reason",     rd.requestdescription AS "Request Description",    frccf.subject AS "Subject",     rqt.requestertypename AS "Applicant Type",    frccf.portfolioofficer AS "Portfolio Officer",     frccf.judicialreview AS "Judicial Review",     rd.status AS "Request Status",    rs.requeststatusname AS "Request Status Name",    eco.officecode AS procorg   FROM "factRequestDetails" rd     LEFT JOIN "dimRequests" r ON rd.foirequestid = r.foirequestid     LEFT JOIN "dimRequesterTypes" rqt ON rd.applicantcategoryid = rqt.requestertypeid     LEFT JOIN "dimRequestStatuses" rs ON rd.requeststatusid = rs.requeststatusid     LEFT JOIN "dimECOffice" eco ON rd.officeid = eco.officeid 	 LEFT JOIN public."factRequestCustomCalcFields" frccf on rd.foirequestid = frccf.foirequestid  WHERE rd.requesttypeid = (( SELECT rt.requesttypeid           FROM "dimRequestTypes" rt          WHERE rt.requesttypename::text = \'Review\'::text)) AND rd.activeflag = \'Y\'::bpchar; ALTER TABLE public.viw_activeoipcreviews OWNER TO postgres; GRANT ALL ON TABLE public.viw_activeoipcreviews TO postgres; GRANT SELECT ON TABLE public.viw_activeoipcreviews TO redash_role;')


def downgrade():
    op.execute('DROP VIEW public.viw_activeoipcreviews; CREATE OR REPLACE VIEW public.viw_activeoipcreviews AS SELECT r.visualrequestfilenumber AS "Request ID", frccf.oipcno AS "OIPC No", rd.primaryusername AS "Primary User", rd.startdate AS "Start Date", rd.targetdate AS "Due Date", frccf.reviewtype AS "Review Type",     frccf.customfieldstatus AS "Status",     frccf.reason AS "Reason",     rd.requestdescription AS "Request Description",    frccf.subject AS "Subject",     rqt.requestertypename AS "Applicant Type",    frccf.portfolioofficer AS "Portfolio Officer",     frccf.judicialreview AS "Judicial Review",     rd.status AS "Request Status",    rs.requeststatusname AS "Request Status Name",    eco.officecode AS procorg   FROM "factRequestDetails" rd     LEFT JOIN "dimRequests" r ON rd.foirequestid = r.foirequestid     LEFT JOIN "dimRequesterTypes" rqt ON rd.applicantcategoryid = rqt.requestertypeid     LEFT JOIN "dimRequestStatuses" rs ON rd.requeststatusid = rs.requeststatusid     LEFT JOIN "dimECOffice" eco ON rd.officeid = eco.officeid 	 LEFT JOIN public."factRequestCustomCalcFields" frccf on rd.foirequestid = frccf.foirequestid  WHERE rd.requesttypeid = (( SELECT rt.requesttypeid           FROM "dimRequestTypes" rt          WHERE rt.requesttypename::text = \'Review\'::text)) AND rd.activeflag = \'Y\'::bpchar; ALTER TABLE public.viw_activeoipcreviews OWNER TO postgres; GRANT ALL ON TABLE public.viw_activeoipcreviews TO postgres; GRANT SELECT ON TABLE public.viw_activeoipcreviews TO redash_role;')
