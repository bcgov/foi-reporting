"""factRequestDocumentsDetails

Revision ID: 4c38b7842c30
Revises: 826627900ca5
Create Date: 2022-01-30 12:28:01.654344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c38b7842c30'
down_revision = '826627900ca5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('factRequestDocumentsDetails',
		sa.Column('foirequestid', sa.Integer(), nullable=False),
		sa.Column('runcycleid', sa.Integer(), nullable=False),
		sa.Column('noofpagesreviewed', sa.Integer()),
		sa.Column('noofpagesreleased', sa.Integer()),
		sa.Column('noofpagesdeduplicated', sa.Integer()),
		sa.Column('noofpagesintherequest', sa.Integer()),
		sa.Column('electronicpageestimate', sa.VARCHAR(length=1000)),
		sa.Column('physicalpageestimate', sa.VARCHAR(length=1000)),
		sa.Column('noofpagesinreviewlog', sa.Integer()),
		sa.Column('noofpagesinredactionlayer', sa.Integer()),
		sa.ForeignKeyConstraint(['runcycleid'], ['dimRunCycle.runcycleid']),
		sa.ForeignKeyConstraint(['foirequestid'], ['dimRequests.foirequestid']),
		sa.PrimaryKeyConstraint('foirequestid','runcycleid')
    )


def downgrade():
    op.drop_table('factRequestDocumentsDetails')
