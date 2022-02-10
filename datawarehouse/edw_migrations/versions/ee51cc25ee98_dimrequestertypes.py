"""dimRequesterTypes

Revision ID: ee51cc25ee98
Revises: 
Create Date: 2022-01-26 17:07:24.717227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee51cc25ee98'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimRequesterTypes',
		sa.Column('requestertypeid', sa.Integer(), nullable=False),
		sa.Column('requestertypename', sa.VARCHAR(length=3000)),
		sa.Column('requestertypedescription', sa.VARCHAR(length=255)),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifieddate', sa.DateTime()),
		sa.Column('creport', sa.CHAR(length=1)),
		sa.Column('cpal', sa.CHAR(length=1)),
		sa.Column('cactive', sa.CHAR(length=1)),
		sa.Column('sortorder', sa.Integer()),
		sa.PrimaryKeyConstraint('requestertypeid')
    )


def downgrade():
    op.drop_table('dimRequesterTypes')
