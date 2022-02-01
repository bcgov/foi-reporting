"""factRequestForDocuments

Revision ID: 489ca98de532
Revises: d6c3af32b13e
Create Date: 2022-01-26 22:39:14.403851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '489ca98de532'
down_revision = 'd6c3af32b13e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('factRequestForDocuments',
		sa.Column('actionid', sa.Integer(), nullable=False),
		sa.Column('foirequestid', sa.Integer(), nullable=False),
		sa.Column('runcycleid', sa.Integer(), nullable=False),
		sa.Column('actiontype', sa.Integer()),
		sa.Column('description', sa.VARCHAR(length=4000)),
		sa.Column('priority', sa.VARCHAR(length=3000)),
		sa.Column('emailaddress', sa.VARCHAR(length=4000)),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('actiondate', sa.DateTime()),
		sa.Column('duedate', sa.DateTime()),
		sa.Column('responsedate', sa.DateTime()),
		sa.Column('parentactionid', sa.Integer()),
		sa.Column('createdby', sa.VARCHAR(length=200)),
		sa.Column('subject', sa.VARCHAR(length=150)),
		sa.Column('programofficeid', sa.Integer()),
		sa.Column('reqfordocstatusid', sa.Integer()),
		sa.Column('completeddate', sa.DateTime()),
		sa.Column('requestofficeid', sa.Integer()),
		sa.Column('visiblerequestid', sa.VARCHAR(length=50)),
		sa.Column('requestdescription', sa.VARCHAR(length=4000)),
		sa.Column('officeid', sa.Integer()),
		sa.Column('requesttypeid', sa.Integer()),
		sa.Column('overduedays', sa.Integer()),
		sa.Column('elapseddays', sa.Integer()),
		sa.Column('passduedays', sa.Integer()),
		sa.Column('rfdage', sa.Integer()),
		sa.Column('remainingdays', sa.Integer()),
		sa.Column('methodofdelivery', sa.VARCHAR(length=1)),
		sa.ForeignKeyConstraint(['reqfordocstatusid'], ['dimRequestForDocumentsStatus.reqfordocstatusid']),
		sa.PrimaryKeyConstraint('actionid', 'foirequestid', 'runcycleid')
    )


def downgrade():
    op.drop_table('factRequestForDocuments')
