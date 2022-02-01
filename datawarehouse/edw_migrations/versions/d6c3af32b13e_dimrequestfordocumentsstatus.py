"""dimRequestForDocumentsStatus

Revision ID: d6c3af32b13e
Revises: 0d832d32eb74
Create Date: 2022-01-26 22:38:17.256795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6c3af32b13e'
down_revision = '0d832d32eb74'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimRequestForDocumentsStatus',
		sa.Column('reqfordocstatusid', sa.Integer(), nullable=False),
		sa.Column('reqfordocstatus', sa.VARCHAR(length=3000)),
		sa.Column('description', sa.VARCHAR(length=255)),
		sa.Column('cactive', sa.CHAR(length=1)),
		sa.Column('cimport', sa.CHAR(length=1)),
		sa.Column('createdby', sa.Integer()),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifiedby', sa.Integer()),
		sa.Column('modifieddate', sa.DateTime()),
		sa.Column('ctype', sa.CHAR(length=1)),
		sa.Column('cmarkcompleted', sa.CHAR(length=1)),
		sa.PrimaryKeyConstraint('reqfordocstatusid')
    )


def downgrade():
    op.drop_table('dimRequestForDocumentsStatus')
