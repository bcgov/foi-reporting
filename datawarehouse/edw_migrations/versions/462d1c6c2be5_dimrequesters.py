"""dimRequesters

Revision ID: 462d1c6c2be5
Revises: ee51cc25ee98
Create Date: 2022-01-26 17:08:26.251136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '462d1c6c2be5'
down_revision = 'ee51cc25ee98'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimRequesters',
		sa.Column('requesterid', sa.Integer(), nullable=False),
		sa.Column('firstname', sa.VARCHAR(length=50)),
		sa.Column('lastname', sa.VARCHAR(length=50)),
		sa.Column('middlename', sa.VARCHAR(length=40)),
		sa.Column('fullname', sa.VARCHAR(length=110)),
		sa.Column('jobtitle', sa.VARCHAR(length=250)),
		sa.Column('addressline1', sa.VARCHAR(length=240)),
		sa.Column('addressline2', sa.VARCHAR(length=160)),
		sa.Column('city', sa.VARCHAR(length=50)),
		sa.Column('zipcode', sa.VARCHAR(length=20)),
		sa.Column('statecode', sa.VARCHAR(length=5)),
		sa.Column('statename', sa.VARCHAR(length=3000)),
		sa.Column('countryname', sa.VARCHAR(length=3000)),
		sa.Column('workphone1', sa.VARCHAR(length=50)),
		sa.Column('workphone2', sa.VARCHAR(length=50)),
		sa.Column('mobile', sa.VARCHAR(length=50)),
		sa.Column('home', sa.VARCHAR(length=50)),
		sa.Column('fax', sa.VARCHAR(length=50)),
		sa.Column('email', sa.VARCHAR(length=500)),
		sa.Column('company', sa.VARCHAR(length=200)),
		sa.Column('notes', sa.VARCHAR(length=2000)),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifieddate', sa.DateTime()),
		sa.Column('cactive', sa.CHAR(length=1)),
		sa.Column('reasonid', sa.Integer()),
		sa.Column('maildue', sa.CHAR(length=1)),
		sa.PrimaryKeyConstraint('requesterid')
    )


def downgrade():
    op.drop_table('dimRequesters')
