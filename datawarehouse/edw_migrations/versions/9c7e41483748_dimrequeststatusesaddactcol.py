"""dimRequestStatusesaddactcol

Revision ID: 9c7e41483748
Revises: 3d5e0572821c
Create Date: 2022-02-16 16:44:48.994101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c7e41483748'
down_revision = '3d5e0572821c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('dimRequestStatuses', sa.Column('cactive', sa.CHAR(length=1)))


def downgrade():
    op.add_column('dimRequestStatuses', sa.Column('cactive', sa.CHAR(length=1)))
