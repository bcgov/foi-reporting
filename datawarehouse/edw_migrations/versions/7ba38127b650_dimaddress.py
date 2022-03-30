"""dimAddress

Revision ID: 7ba38127b650
Revises: 1cc0deead1b9
Create Date: 2022-02-28 19:57:01.104624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ba38127b650'
down_revision = '1cc0deead1b9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimAddress',
		sa.Column('addressid', sa.Integer(), nullable=False),
		sa.Column('address1', sa.VARCHAR(length=150)),
		sa.Column('address2', sa.VARCHAR(length=80)),
		sa.Column('city', sa.VARCHAR(length=30)),
		sa.Column('state', sa.VARCHAR(length=3000)),
		sa.Column('country', sa.VARCHAR(length=3000)),
		sa.Column('zipcode', sa.CHAR(length=10)),
		sa.PrimaryKeyConstraint('addressid')
    )


def downgrade():
    op.drop_table('dimAddress')
