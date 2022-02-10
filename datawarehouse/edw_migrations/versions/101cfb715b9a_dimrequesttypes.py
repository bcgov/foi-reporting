"""dimRequestTypes

Revision ID: 101cfb715b9a
Revises: 2e97ccf78659
Create Date: 2022-01-26 23:07:13.900897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '101cfb715b9a'
down_revision = '2e97ccf78659'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimRequestTypes',
		sa.Column('requesttypeid', sa.Integer(), nullable=False),
		sa.Column('requesttypename', sa.VARCHAR(length=3000)),
		sa.Column('requesttypecode', sa.VARCHAR(length=4)),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifieddate', sa.DateTime()),
		sa.Column('priority', sa.VARCHAR(length=3000)),
		sa.Column('casetype', sa.CHAR(length=1)),
		sa.Column('acttype', sa.CHAR(length=1)),
		sa.Column('acttypename', sa.VARCHAR(length=50)),
		sa.Column('cdelete', sa.CHAR(length=1)),
		sa.Column('siretentionpolicyid', sa.Integer()),
		sa.Column('cIsconsultation', sa.CHAR(length=1)),
		sa.Column('cIslitigation', sa.CHAR(length=1)),
		sa.Column('timultitracktype', sa.Integer()),
		sa.Column('tiprocessingdays', sa.Integer()),
		sa.Column('tisimpleprocessingdays', sa.Integer()),
		sa.Column('ticomplexprocessingdays', sa.Integer()),
		sa.Column('tiexpediteprocessingdays', sa.Integer()),
		sa.Column('csimpleprocessingdays', sa.CHAR(length=1)),
		sa.Column('ccomplexprocessingdays', sa.CHAR(length=1)),
		sa.Column('cexpediteprocessingdays', sa.CHAR(length=1)),
		sa.Column('cshowinhomepage', sa.CHAR(length=1)),
		sa.Column('cactsubtype', sa.CHAR(length=1)),
		sa.Column('tiapplicablesection', sa.Integer()),
		sa.Column('cactive', sa.CHAR(length=1)),
		sa.Column('cconsultationtype', sa.CHAR(length=1)),
		sa.Column('cenableapprovalpackage', sa.CHAR(length=1)),
		sa.Column('iduplicatesearchoptions', sa.Integer()),
		sa.PrimaryKeyConstraint('requesttypeid')
    )


def downgrade():
    op.drop_table('dimRequestTypes')
