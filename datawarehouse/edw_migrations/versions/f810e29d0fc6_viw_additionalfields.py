"""empty message

Revision ID: f810e29d0fc6
Revises: 48ca4d3043a2
Create Date: 2022-03-23 11:01:19.401377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f810e29d0fc6'
down_revision = '48ca4d3043a2'
branch_labels = None
depends_on = None


def upgrade():
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


def downgrade():
    op.execute('DROP VIEW public.viw_additionalfields; ')