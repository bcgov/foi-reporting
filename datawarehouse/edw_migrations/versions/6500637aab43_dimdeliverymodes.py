"""dimDeliveryModes

Revision ID: 6500637aab43
Revises: 12ddff140788
Create Date: 2022-01-26 23:23:58.449449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6500637aab43'
down_revision = '12ddff140788'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dimDeliveryModes',
		sa.Column('deliverymodeid', sa.Integer(), nullable=False),
		sa.Column('deliverymodename', sa.VARCHAR(length=3000)),
		sa.Column('cactive', sa.CHAR(length=1)),
		sa.Column('createddate', sa.DateTime()),
		sa.Column('modifieddate', sa.DateTime()),
		sa.Column('cdelete', sa.CHAR(length=1)),
		sa.Column('cpal', sa.CHAR(length=1)),
		sa.Column('cdefault', sa.CHAR(length=1)),
		sa.PrimaryKeyConstraint('deliverymodeid')
    )


def downgrade():
    op.drop_table('dimDeliveryModes')
