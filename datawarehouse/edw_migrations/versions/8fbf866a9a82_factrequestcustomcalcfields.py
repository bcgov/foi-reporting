"""empty message

Revision ID: 8fbf866a9a82
Revises: e902c9221d33
Create Date: 2022-03-15 16:44:00.797887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fbf866a9a82'
down_revision = 'e902c9221d33'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('factRequestCustomCalcFields',
		sa.Column('foirequestid', sa.Integer(), nullable=False),
		sa.Column('runcycleid', sa.Integer(), nullable=False),
		sa.Column('identityverification', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('previousfoirequest', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('applicationfeepaid', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('applicationfeerefunded', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('applicationfeetransferred', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('linkedrequests', sa.VARCHAR(length=3000), nullable=True),
        sa.Column('feepaidamount', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('refundamount', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('prepaymentamount', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('physicalpageestimate', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('electronicpageestimate', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('customfieldstatus', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('secondaryusers', sa.VARCHAR(length=3000), nullable=True),
        sa.Column('applicantfilereference', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('coordinatednrresponsereqd', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('portfolioofficer', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('reason', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('reviewtype', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('judicialreview', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('oipcno', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('publicationreason', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('publication', sa.VARCHAR(length=1000), nullable=True),      
        sa.Column('crossgovtno', sa.VARCHAR(length=1000), nullable=True),    
        sa.Column('subject', sa.VARCHAR(length=1000), nullable=True),
        sa.Column('currentactivitydate', sa.DateTime(), nullable=True),
        sa.Column('noofdocdelivered', sa.Integer, nullable=True),
        sa.Column('onholddays', sa.Integer, nullable=True),
        sa.Column('countontime', sa.Integer, nullable=True),
        sa.Column('countoverdue', sa.Integer, nullable=True),
        sa.Column('daysoverdue', sa.Integer, nullable=True),
        sa.Column('passduedays', sa.Integer, nullable=True),
        sa.Column('noofpagesreviewed', sa.Integer, nullable=True),
        sa.Column('noofpagesreleased', sa.Integer, nullable=True),
        sa.Column('noofpagesdeduplicated', sa.Integer, nullable=True),

		sa.ForeignKeyConstraint(['runcycleid'], ['dimRunCycle.runcycleid']),
		sa.ForeignKeyConstraint(['foirequestid'], ['dimRequests.foirequestid']),		
    )


def downgrade():
    op.drop_table('factRequestCustomCalcFields')
