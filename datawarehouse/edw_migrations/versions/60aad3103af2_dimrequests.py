"""dimRequests

Revision ID: 60aad3103af2
Revises: 74dd3c263cb8
Create Date: 2022-01-27 00:04:23.082986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60aad3103af2'
down_revision = '74dd3c263cb8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimRequests',
		sa.Column('foirequestid', sa.Integer(), nullable=False),
		sa.Column('sourceoftruth', sa.VARCHAR(length=50)),
		sa.Column('sourceoftruthuniqueid', sa.Integer()),
		sa.Column('visualrequestfilenumber', sa.VARCHAR(length=50)),
		sa.Column('cactive', sa.CHAR(length=1)),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifieddate', sa.DateTime()),
		sa.Column('requestdescription', sa.VARCHAR(length=4000)),
		sa.Column('priority', sa.VARCHAR(length=3000)),
		sa.Column('requesterid', sa.Integer()),
		sa.Column('onbehalfofrequesterid', sa.Integer()),
		sa.Column('referencenumber', sa.Integer()),
		sa.Column('refvisualrequestfilenumber', sa.VARCHAR(length=50)),
		sa.PrimaryKeyConstraint('foirequestid')
    )


def downgrade():
    op.drop_table('dimRequests')
