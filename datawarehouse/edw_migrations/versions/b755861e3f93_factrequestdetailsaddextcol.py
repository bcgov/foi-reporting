"""factRequestDetailsaddextcol

Revision ID: b755861e3f93
Revises: 9c7e41483748
Create Date: 2022-02-16 16:45:32.681275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b755861e3f93'
down_revision = '9c7e41483748'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('factRequestDetails', sa.Column('extension', sa.Integer()))


def downgrade():
    op.add_column('factRequestDetails', sa.Column('extension', sa.Integer()))
