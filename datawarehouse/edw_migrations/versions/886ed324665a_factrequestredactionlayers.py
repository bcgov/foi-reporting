"""factRequestRedactionLayers

Revision ID: 886ed324665a
Revises: 224658c1de31
Create Date: 2022-01-30 16:09:19.702040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '886ed324665a'
down_revision = '224658c1de31'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('factRequestRedactionLayers',
		sa.Column('foirequestid', sa.Integer(), nullable=False),
		sa.Column('runcycleid', sa.Integer(), nullable=False),
		sa.Column('redactlayerid', sa.Integer(), nullable=False),
		sa.Column('docid', sa.Integer()),
		sa.Column('docname', sa.VARCHAR(length=200)),
		sa.Column('sectionlist', sa.VARCHAR(length=4000)),
		sa.Column('comments', sa.VARCHAR(length=4000)),
		sa.Column('requestdocid', sa.Integer()),
		sa.Column('reqdocdescription', sa.VARCHAR(length=1000)),
		sa.Column('reqdocnotes', sa.VARCHAR(length=4000)),
		sa.Column('reqdocstatus', sa.VARCHAR(length=50)),
		sa.Column('deliveryid', sa.Integer()),
		sa.Column('refredactlayerid', sa.Integer()),
		sa.Column('docreviewstatusid', sa.Integer()),
		sa.Column('docreviewstatus', sa.VARCHAR(length=3000)),
		sa.Column('cactive', sa.CHAR(length=1)),
		sa.Column('parentdocid', sa.Integer()),
		sa.Column('isredacted', sa.CHAR(length=1)),
		sa.Column('pagecount', sa.Integer()),
		sa.Column('maxpagenum', sa.Integer()),
		sa.Column('statuscode', sa.Integer()),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifieddate', sa.DateTime()),
		sa.Column('cfr', sa.CHAR(length=1)),
		sa.ForeignKeyConstraint(['runcycleid'], ['dimRunCycle.runcycleid']),
		sa.ForeignKeyConstraint(['foirequestid'], ['dimRequests.foirequestid']),
		sa.PrimaryKeyConstraint('redactlayerid')
    )


def downgrade():
    op.drop_table('factRequestRedactionLayers')
