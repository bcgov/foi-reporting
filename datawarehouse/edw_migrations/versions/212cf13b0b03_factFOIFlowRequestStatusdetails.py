"""empty message

Revision ID: 212cf13b0b03
Revises: 4eaf6c1c9c49
Create Date: 2022-07-12 13:59:04.194069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '212cf13b0b03'
down_revision = '4eaf6c1c9c49'
branch_labels = None
depends_on = None


def upgrade():
      op.create_table('factFOIFlowRequestStatusDetails',
		sa.Column('foiflowrequeststatusdetailsid', sa.Integer(), nullable=False),
		sa.Column('runcycleid', sa.Integer(), nullable=False),       
        sa.Column('foirequestnumber', sa.VARCHAR(length=120), nullable=False),                
        sa.Column('version', sa.Integer(), nullable=False),	
        sa.Column('isactive', sa.Boolean()),

        sa.Column('requeststatusid', sa.Integer()),
        sa.Column('ministrycode', sa.VARCHAR(length=120)),

        sa.Column('assignedgroup', sa.VARCHAR(length=250)),
        sa.Column('assignedministryperson', sa.VARCHAR(length=250)),
        sa.Column('assignedministrygroup', sa.VARCHAR(length=250)),

        sa.Column('startdate', sa.DateTime()),
        sa.Column('duedate', sa.DateTime()),
        sa.Column('cfrduedate', sa.DateTime()),
        sa.Column('closedate', sa.DateTime()),

		sa.Column('createdby', sa.VARCHAR(length=50)),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifiedby', sa.VARCHAR(length=50)),
		sa.Column('modifieddate', sa.DateTime()),

		sa.ForeignKeyConstraint(['runcycleid'], ['dimRunCycle.runcycleid']),	
		sa.PrimaryKeyConstraint('foiflowrequeststatusdetailsid','runcycleid','version')
      )

def downgrade():
    op.drop_table('factFOIFlowRequestStatusDetails')
