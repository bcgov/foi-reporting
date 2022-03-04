"""update dimruncycle

Revision ID: e6f1bd521efc
Revises: 09334b5ca2df
Create Date: 2022-02-28 15:27:00.514858

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = 'e6f1bd521efc'
down_revision = '09334b5ca2df'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('dimRunCycle', 'runcycledatetime', new_column_name='runcyclestartat')
    op.add_column('dimRunCycle', sa.Column('packageid', sa.VARCHAR(100), nullable=True))
    op.add_column('dimRunCycle', sa.Column('packagename', sa.VARCHAR(100), nullable=True))
    op.add_column('dimRunCycle', sa.Column('runcycleendat', sa.DateTime(), nullable=True, default=datetime.now()))
    op.add_column('dimRunCycle', sa.Column('success', sa.Boolean(), nullable=True))


def downgrade():
    op.alter_column('dimRunCycle', 'runcyclestartat', new_column_name='runcycledatetime')
    op.drop_column('dimRunCycle', 'packageid')
    op.drop_column('dimRunCycle', 'packagename')
    op.drop_column('dimRunCycle', 'runcycleenddate')
    op.drop_column('dimRunCycle', 'success')
