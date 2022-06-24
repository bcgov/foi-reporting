"""empty message

Revision ID: 36c90c6093f0
Revises: a010fb34347d
Create Date: 2022-06-24 11:15:20.645010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36c90c6093f0'
down_revision = 'a010fb34347d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimStages',
		sa.Column('stageid', sa.Integer(), nullable=False),
		sa.Column('name', sa.VARCHAR(length=500)),
		sa.Column('description', sa.TEXT),
		sa.Column('cactive', sa.CHAR(length=1)),
		sa.PrimaryKeyConstraint('stageid')
    )


def downgrade():
    op.drop_table('dimStages')
