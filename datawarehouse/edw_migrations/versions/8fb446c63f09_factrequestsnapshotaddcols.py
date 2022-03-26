"""factRequestSnapshotAddCols

Revision ID: 8fb446c63f09
Revises: 2e6cf8a26f8f
Create Date: 2022-03-25 12:04:21.151446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fb446c63f09'
down_revision = '2e6cf8a26f8f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('factRequestSnapshot',sa.Column('currentactivity', sa.VARCHAR(length=4000)))
    op.add_column('factRequestSnapshot',sa.Column('officecode', sa.VARCHAR(length=3000)))
    op.add_column('factRequestSnapshot',sa.Column('officedescription', sa.VARCHAR(length=2000)))


def downgrade():
    op.add_column('factRequestSnapshot',sa.Column('currentactivity', sa.VARCHAR(length=4000)))
    op.add_column('factRequestSnapshot',sa.Column('officecode', sa.VARCHAR(length=3000)))
    op.add_column('factRequestSnapshot',sa.Column('officedescription', sa.VARCHAR(length=2000)))
