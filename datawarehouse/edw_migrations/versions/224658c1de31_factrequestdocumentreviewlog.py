"""factRequestDocumentReviewLog

Revision ID: 224658c1de31
Revises: 4c38b7842c30
Create Date: 2022-01-30 16:00:33.038416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '224658c1de31'
down_revision = '4c38b7842c30'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('factRequestDocumentReviewLog',
		sa.Column('foirequestid', sa.Integer(), nullable=False),
		sa.Column('runcycleid', sa.Integer(), nullable=False),
		sa.Column('docid', sa.Integer(), nullable=False),
		sa.Column('docname', sa.VARCHAR(length=200)),
		sa.Column('sectionlist', sa.VARCHAR(length=4000)),
		sa.Column('comments', sa.VARCHAR(length=4000)),
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
		sa.PrimaryKeyConstraint('docid')
    )


def downgrade():
    op.drop_table('factRequestDocumentReviewLog')
