"""dimExtensionTypes

Revision ID: 243b2aa7349a
Revises: ff22f9ed7af8
Create Date: 2022-01-26 17:39:06.035464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '243b2aa7349a'
down_revision = 'ff22f9ed7af8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimExtensionTypes',
		sa.Column('extensiontypeid', sa.Integer(), nullable=False),
		sa.Column('extensiontypename', sa.VARCHAR(length=3000)),
		sa.Column('createdby', sa.Integer()),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifiedby', sa.Integer()),
		sa.Column('modifieddate', sa.DateTime()),
		sa.Column('cactive', sa.CHAR(length=1)),
		sa.Column('cdelete', sa.CHAR(length=1)),
		sa.Column('cacttype', sa.CHAR(length=1)),
		sa.Column('extensionreason', sa.VARCHAR(length=3000)),
		sa.Column('extensionactdesc', sa.VARCHAR(length=3000)),
		sa.Column('vcshowninsr', sa.VARCHAR(length=100)),
		sa.Column('clsthirdparty', sa.CHAR(length=1)),
		sa.Column('vcdaysallowed', sa.VARCHAR(length=10)),
		sa.Column('iextensiondays', sa.Integer()),
		sa.PrimaryKeyConstraint('extensiontypeid')
    )


def downgrade():
    op.drop_table('dimExtensionTypes')
