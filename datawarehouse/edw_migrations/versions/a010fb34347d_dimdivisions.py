"""dimDivisions

Revision ID: a010fb34347d
Revises: e6460d4979c4
Create Date: 2022-06-24 10:50:20.543192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a010fb34347d'
down_revision = 'ea59d5c1f1c0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimDivisions',
		sa.Column('divisionid', sa.Integer(), nullable=False),
		sa.Column('division', sa.VARCHAR(length=500)),
		sa.Column('description', sa.TEXT),
		sa.Column('cactive', sa.CHAR(length=1)),
		sa.PrimaryKeyConstraint('divisionid')
    )


def downgrade():
    op.drop_table('dimDivisions')
