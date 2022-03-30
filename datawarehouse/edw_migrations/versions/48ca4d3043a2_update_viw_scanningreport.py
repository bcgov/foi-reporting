"""update_viw_scanningreport

Revision ID: 48ca4d3043a2
Revises: 58c33fb2322c
Create Date: 2022-03-17 14:57:20.645563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48ca4d3043a2'
down_revision = '58c33fb2322c'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('DROP VIEW public.viw_scanningreport; CREATE OR REPLACE VIEW public.viw_scanningreport AS SELECT r.visualrequestfilenumber AS "Request ID",    rd.extension AS "# of Extensions Applied",    frccf.physicalpageestimate AS "Physical Page Estimate",    frccf.electronicpageestimate AS "Electronic Page Estimate",    rd.remainingdays AS "Remaining Days",    rd.targetdate AS "Due Date",    rd.primaryusername AS "Primary User"   FROM "factRequestDetails" rd     LEFT JOIN "dimRequests" r ON rd.foirequestid = r.foirequestid     LEFT JOIN "factRequestDocumentsDetails" rdd ON rdd.foirequestid = rd.foirequestid AND rdd.activeflag = \'Y\'::bpchar 	 LEFT JOIN public."factRequestCustomCalcFields" frccf on rd.foirequestid = frccf.foirequestid  WHERE rd.activeflag = \'Y\'::bpchar;ALTER TABLE public.viw_scanningreport    OWNER TO postgres;GRANT ALL ON TABLE public.viw_scanningreport TO postgres;GRANT SELECT ON TABLE public.viw_scanningreport TO redash_role;')


def downgrade():
    op.execute('DROP VIEW public.viw_scanningreport; CREATE OR REPLACE VIEW public.viw_scanningreport AS SELECT r.visualrequestfilenumber AS "Request ID",    rd.extension AS "# of Extensions Applied",    frccf.physicalpageestimate AS "Physical Page Estimate",    frccf.electronicpageestimate AS "Electronic Page Estimate",    rd.remainingdays AS "Remaining Days",    rd.targetdate AS "Due Date",    rd.primaryusername AS "Primary User"   FROM "factRequestDetails" rd     LEFT JOIN "dimRequests" r ON rd.foirequestid = r.foirequestid     LEFT JOIN "factRequestDocumentsDetails" rdd ON rdd.foirequestid = rd.foirequestid AND rdd.activeflag = \'Y\'::bpchar 	 LEFT JOIN public."factRequestCustomCalcFields" frccf on rd.foirequestid = frccf.foirequestid  WHERE rd.activeflag = \'Y\'::bpchar;ALTER TABLE public.viw_scanningreport    OWNER TO postgres;GRANT ALL ON TABLE public.viw_scanningreport TO postgres;GRANT SELECT ON TABLE public.viw_scanningreport TO redash_role;')
