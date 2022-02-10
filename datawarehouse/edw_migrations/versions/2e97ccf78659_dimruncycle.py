"""dimRunCycle

Revision ID: 2e97ccf78659
Revises: 489ca98de532
Create Date: 2022-01-26 22:47:33.536424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e97ccf78659'
down_revision = '489ca98de532'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimRunCycle',
		sa.Column('runcycleid', sa.Integer(), nullable=False),
		sa.Column('runcycledatetime', sa.DateTime()),
		sa.Column('description', sa.VARCHAR(length=3000)),
		sa.PrimaryKeyConstraint('runcycleid')
    )


def downgrade():
    op.drop_table('dimRunCycle')
