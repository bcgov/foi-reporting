"""empty message

Revision ID: b25c9f49e1f1
Revises: 8fbf866a9a82
Create Date: 2022-03-16 12:35:56.673754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b25c9f49e1f1'
down_revision = '8fbf866a9a82'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('factRequestRFDCalculatedFields',
		sa.Column('foirequestid', sa.Integer(), nullable=False),
		sa.Column('runcycleid', sa.Integer(), nullable=False),
        sa.Column('actionid', sa.Integer(), nullable=True),
        sa.Column('overduedays', sa.Integer(), nullable=True),
        sa.Column('elapseddays', sa.Integer(), nullable=True),
        sa.Column('passduedays', sa.Integer(), nullable=True),
        sa.Column('rfdage', sa.Integer(), nullable=True),
        sa.Column('remainingdays', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['runcycleid'], ['dimRunCycle.runcycleid']),
		sa.ForeignKeyConstraint(['foirequestid'], ['dimRequests.foirequestid'])		
    )

def downgrade():
    op.drop_table('factRequestRFDCalculatedFields')
