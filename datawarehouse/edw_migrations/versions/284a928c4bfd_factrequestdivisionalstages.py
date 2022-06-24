"""empty message

Revision ID: 284a928c4bfd
Revises: 36c90c6093f0
Create Date: 2022-06-24 11:22:11.361691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '284a928c4bfd'
down_revision = '36c90c6093f0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('factRequestDivisionalStages',
		sa.Column('foirequestdivisionstageid', sa.Integer(), nullable=False),
		sa.Column('runcycleid', sa.Integer(), nullable=False),
        sa.Column('divisionid', sa.Integer(), nullable=False),
        sa.Column('stageid', sa.Integer(), nullable=False),	
        sa.Column('foirequestid', sa.Integer(), nullable=False),
        sa.Column('officeid', sa.Integer(), nullable=False),	
		sa.Column('createdby', sa.Integer()),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifiedby', sa.Integer()),
		sa.Column('modifieddate', sa.DateTime()),
		sa.Column('divisionstageduedate', sa.DateTime()),
        sa.Column('divisionstagereceiveddate', sa.DateTime()),
        sa.Column('divisionstageeapproval', sa.CHAR(length=15)),
		sa.ForeignKeyConstraint(['runcycleid'], ['dimRunCycle.runcycleid']),
		sa.ForeignKeyConstraint(['foirequestid'], ['dimRequests.foirequestid']),
        sa.ForeignKeyConstraint(['divisionid'], ['dimDivisions.divisionid']),
        sa.ForeignKeyConstraint(['stageid'], ['dimStages.stageid']),
        sa.ForeignKeyConstraint(['officeid'], ['dimECOffice.officeid']),
		sa.PrimaryKeyConstraint('foirequestdivisionstageid','runcycleid')
    )


def downgrade():
    op.drop_table('factRequestDivisionalStages')
