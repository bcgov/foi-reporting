"""dimECOffice

Revision ID: 907f2e75c0e5
Revises: c823b454a375
Create Date: 2022-01-27 00:21:45.343369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '907f2e75c0e5'
down_revision = 'c823b454a375'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimECOffice',
		sa.Column('officeid', sa.Integer(), nullable=False),
		sa.Column('officecode', sa.VARCHAR(length=3000)),
		sa.Column('officedescription', sa.VARCHAR(length=2000)),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifieddate', sa.DateTime()),
		sa.Column('emailid', sa.VARCHAR(length=255)),
		sa.Column('pal', sa.CHAR(length=1)),
		sa.Column('corraddress1', sa.VARCHAR(length=150)),
		sa.Column('corraddress2', sa.VARCHAR(length=80)),
		sa.Column('corrphonenumber', sa.VARCHAR(length=30)),
		sa.Column('corrcity', sa.VARCHAR(length=30)),
		sa.Column('corrzipcode', sa.VARCHAR(length=10)),
		sa.Column('corrstatename', sa.VARCHAR(length=3000)),
		sa.Column('corrstatecode', sa.CHAR(length=5)),
		sa.Column('corrcountry', sa.VARCHAR(length=3000)),
		sa.Column('remittaddress1', sa.VARCHAR(length=150)),
		sa.Column('remittaddress2', sa.VARCHAR(length=80)),
		sa.Column('remittcity', sa.VARCHAR(length=30)),
		sa.Column('remittzipcode', sa.VARCHAR(length=10)),
		sa.Column('remittstatename', sa.VARCHAR(length=3000)),
		sa.Column('remittstatecode', sa.CHAR(length=5)),
		sa.Column('remittcountry', sa.VARCHAR(length=3000)),
		sa.Column('parentofficedesc', sa.VARCHAR(length=2000)),
		sa.Column('officenameforpal', sa.VARCHAR(length=1000)),
		sa.Column('starttime', sa.VARCHAR(length=10)),
		sa.Column('endtime', sa.VARCHAR(length=10)),
		sa.Column('headofoffice', sa.Integer()),
		sa.Column('officecoordinator', sa.VARCHAR(length=30)),
		sa.Column('officealternate', sa.VARCHAR(length=100)),
		sa.Column('faxno', sa.VARCHAR(length=30)),
		sa.Column('alternateofficefax', sa.VARCHAR(length=30)),
		sa.Column('alternateofficephone', sa.VARCHAR(length=30)),
		sa.Column('invitationcontact', sa.VARCHAR(length=100)),
		sa.Column('invitationcontactperson', sa.VARCHAR(length=100)),
		sa.Column('isactive', sa.CHAR(length=1)),
		sa.Column('displayname', sa.VARCHAR(length=2000)),
		sa.Column('displaynameformat', sa.Integer()),
		sa.Column('tenantid', sa.Integer()),
		sa.PrimaryKeyConstraint('officeid')
    )


def downgrade():
    op.drop_table('dimECOffice')
