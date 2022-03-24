"""empty message

Revision ID: adb323f88d99
Revises: f810e29d0fc6
Create Date: 2022-03-23 15:23:31.537164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adb323f88d99'
down_revision = 'f810e29d0fc6'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('DROP VIEW public.viw_additionalfields;CREATE OR REPLACE VIEW public.viw_additionalfields AS '\
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


def downgrade():
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
 ' WHERE rd.activeflag = \'Y\'::bpchar; ')