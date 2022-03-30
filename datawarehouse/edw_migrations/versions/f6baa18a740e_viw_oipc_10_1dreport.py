"""viw_oipc_10_1dreport

Revision ID: f6baa18a740e
Revises: 336bfa51f077
Create Date: 2022-02-28 19:59:59.063697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6baa18a740e'
down_revision = '336bfa51f077'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE OR REPLACE VIEW public.viw_oipc_10_1dreport AS SELECT r.visualrequestfilenumber AS "Request ID", rd.targetdate AS "Due Date", re.extendeddate AS "Proposed Date", rd.primaryusername AS "Primary User" FROM "factRequestDetails" rd LEFT JOIN "dimRequests" r ON rd.foirequestid = r.foirequestid JOIN "factRequestExtensions" re ON re.foirequestid = rd.foirequestid and re.activeflag = \'Y\' LEFT JOIN "dimExtensionTypes" et ON et.extensiontypeid = re.extensiontypeid WHERE rd.activeflag = \'Y\' and et.extensiontypename::text !~~ \'PB%\'::text AND re.cstatus = \'P\'::bpchar ORDER BY r.visualrequestfilenumber;')


def downgrade():
    op.drop_view(viw_oipc_10_1dreport)
