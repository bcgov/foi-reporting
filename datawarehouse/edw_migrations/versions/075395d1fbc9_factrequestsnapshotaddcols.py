"""factRequestSnapshotAddCols

Revision ID: 075395d1fbc9
Revises: 8fb446c63f09
Create Date: 2022-03-28 15:10:04.014433

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '075395d1fbc9'
down_revision = '8fb446c63f09'
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
