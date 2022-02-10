"""dimECGroups

Revision ID: c823b454a375
Revises: 60aad3103af2
Create Date: 2022-01-27 00:10:31.531762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c823b454a375'
down_revision = '60aad3103af2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimECGroups',
		sa.Column('groupid', sa.Integer(), nullable=False),
		sa.Column('groupname', sa.VARCHAR(length=255)),
		sa.Column('tllgroupname', sa.VARCHAR(length=3000)),
		sa.Column('groupdescription', sa.VARCHAR(length=500)),
		sa.Column('isactive', sa.CHAR(length=1)),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifieddate', sa.DateTime()),
		sa.Column('groupcode', sa.VARCHAR(length=4)),
		sa.Column('deleteflag', sa.CHAR(length=1)),
		sa.Column('officeid', sa.Integer()),
		sa.Column('emailid', sa.VARCHAR(length=255)),
		sa.PrimaryKeyConstraint('groupid')
    )


def downgrade():
    op.drop_table('dimECGroups')
