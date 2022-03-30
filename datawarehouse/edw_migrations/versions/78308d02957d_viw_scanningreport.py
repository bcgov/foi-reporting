"""viw_scanningreport

Revision ID: 78308d02957d
Revises: 8bca9f276d1c
Create Date: 2022-02-28 20:03:03.657961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78308d02957d'
down_revision = '8bca9f276d1c'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE OR REPLACE VIEW public.viw_scanningreport AS SELECT r.visualrequestfilenumber AS "Request ID", rd.extension AS "# of Extensions Applied", rdd.physicalpageestimate AS "Physical Page Estimate", rdd.electronicpageestimate AS "Electronic Page Estimate", rd.remainingdays AS "Remaining Days", rd.targetdate AS "Due Date", rd.primaryusername AS "Primary User" FROM "factRequestDetails" rd LEFT JOIN "dimRequests" r ON rd.foirequestid = r.foirequestid LEFT JOIN "factRequestDocumentsDetails" rdd ON rdd.foirequestid = rd.foirequestid and rdd.activeflag = \'Y\' WHERE rd.activeflag = \'Y\';commit;')


def downgrade():
    op.drop_view(viw_scanningreport)
