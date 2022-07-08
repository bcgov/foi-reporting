"""empty message

Revision ID: 054e7c836ebd
Revises: 9a0350f80fd9
Create Date: 2022-07-06 15:24:23.265302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '054e7c836ebd'
down_revision = '9a0350f80fd9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('factRequestDivisionalStages', sa.Column('foirequestversionid', sa.Integer(), nullable=False))
    op.add_column('factRequestDivisionalStages', sa.Column('foiministryrequestid', sa.Integer(), nullable=False))
    op.add_column('factRequestDivisionalStages', sa.Column('foirequestnumber', sa.VARCHAR(length=50), nullable=True))
    op.drop_column('factRequestDivisionalStages', 'foirequestid')

def downgrade():
    op.drop_column('factRequestDivisionalStages', 'foirequestversionid')
    op.drop_column('factRequestDivisionalStages', 'foiministryrequestid')
    op.drop_column('factRequestDivisionalStages', 'foirequestnumber')
    op.add_column('factRequestDivisionalStages', sa.Column('foirequestid', sa.Integer(), nullable=False))
