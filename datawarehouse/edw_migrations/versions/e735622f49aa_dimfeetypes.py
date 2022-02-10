"""dimFeeTypes

Revision ID: e735622f49aa
Revises: 11dbbdfb4ebb
Create Date: 2022-01-27 00:54:21.137823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e735622f49aa'
down_revision = '11dbbdfb4ebb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimFeeTypes',
		sa.Column('feetypeid', sa.Integer(), nullable=False),
		sa.Column('feetypename', sa.VARCHAR(length=3000)),
		sa.Column('feetypedescription', sa.VARCHAR(length=150)),
		sa.Column('sortorder', sa.Integer()),
		sa.Column('cactive', sa.CHAR(length=1)),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifieddate', sa.DateTime()),
		sa.Column('clschangeable', sa.CHAR(length=1)),
		sa.Column('clsindependent', sa.CHAR(length=1)),
		sa.Column('nrate', sa.Numeric(precision=11, scale=2)),
		sa.Column('vcfeecode', sa.VARCHAR(length=2)),
		sa.Column('creport', sa.CHAR(length=1)),
		sa.Column('nfeewaived', sa.Numeric(precision=11, scale=2)),
		sa.Column('sireffeeid', sa.Integer()),
		sa.Column('cadministrativecost', sa.CHAR(length=1)),
		sa.Column('cenable', sa.CHAR(length=1)),
		sa.PrimaryKeyConstraint('feetypeid')
    )


def downgrade():
    op.drop_table('dimFeeTypes')
