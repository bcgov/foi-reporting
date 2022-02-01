"""factRequestRequesters

Revision ID: ff22f9ed7af8
Revises: 462d1c6c2be5
Create Date: 2022-01-26 17:10:09.411302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff22f9ed7af8'
down_revision = '462d1c6c2be5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('factRequestRequesters',
		sa.Column('foirequestid', sa.Integer(), nullable=False),
		sa.Column('runcycleid', sa.Integer(), nullable=False),
		sa.Column('requesttypeid', sa.Integer()),
		sa.Column('applicantcategoryid', sa.Integer()),
		sa.Column('requestertypeid', sa.Integer()),
		sa.Column('requesterid', sa.Integer()),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifieddate', sa.DateTime()),
		sa.ForeignKeyConstraint(['requestertypeid'], ['dimRequesterTypes.requestertypeid']),
		sa.ForeignKeyConstraint(['requesterid'], ['dimRequesters.requesterid']),
		sa.PrimaryKeyConstraint('foirequestid', 'runcycleid')
    )


def downgrade():
    op.drop_table('factRequestRequesters')
