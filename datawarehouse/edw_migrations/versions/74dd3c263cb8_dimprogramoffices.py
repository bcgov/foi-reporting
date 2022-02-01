"""dimProgramOffices

Revision ID: 74dd3c263cb8
Revises: 6500637aab43
Create Date: 2022-01-26 23:52:23.698157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74dd3c263cb8'
down_revision = '6500637aab43'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimProgramOffices',
		sa.Column('programofficeid', sa.Integer(), nullable=False),
		sa.Column('programofficename', sa.VARCHAR(length=3000)),
		sa.Column('corraddress1', sa.VARCHAR(length=150)),
		sa.Column('corraddress2', sa.VARCHAR(length=80)),
		sa.Column('corrcity', sa.VARCHAR(length=30)),
		sa.Column('corrstate', sa.VARCHAR(length=3000)),
		sa.Column('corrstatecode', sa.CHAR(length=5)),
		sa.Column('corrzipcode', sa.VARCHAR(length=10)),
		sa.Column('corrcountry', sa.VARCHAR(length=3000)),
		sa.Column('emailid', sa.VARCHAR(length=4000)),
		sa.Column('phone', sa.VARCHAR(length=25)),
		sa.Column('fax', sa.VARCHAR(length=25)),
		sa.Column('tiofficeid', sa.Integer()),
		sa.Column('ctype', sa.CHAR(length=1)),
		sa.Column('lastname', sa.VARCHAR(length=25)),
		sa.Column('firstname', sa.VARCHAR(length=50)),
		sa.Column('altphone', sa.VARCHAR(length=25)),
		sa.Column('englishtitle', sa.VARCHAR(length=255)),
		sa.Column('ccname', sa.VARCHAR(length=25)),
		sa.Column('ccemail', sa.VARCHAR(length=4000)),
		sa.Column('visibleid', sa.VARCHAR(length=50)),
		sa.Column('company', sa.VARCHAR(length=50)),
		sa.Column('programoffice', sa.CHAR(length=1)),
		sa.Column('consultationoffice', sa.CHAR(length=1)),
		sa.Column('cactive', sa.CHAR(length=1)),
		sa.Column('remaddress1', sa.VARCHAR(length=150)),
		sa.Column('remaddress2', sa.VARCHAR(length=80)),
		sa.Column('remcity', sa.VARCHAR(length=30)),
		sa.Column('remzipcode', sa.VARCHAR(length=10)),
		sa.Column('remstate', sa.VARCHAR(length=3000)),
		sa.Column('remstatecode', sa.CHAR(length=5)),
		sa.Column('remcountry', sa.VARCHAR(length=3000)),
		sa.PrimaryKeyConstraint('programofficeid')
    )


def downgrade():
    op.drop_table('dimProgramOffices')
