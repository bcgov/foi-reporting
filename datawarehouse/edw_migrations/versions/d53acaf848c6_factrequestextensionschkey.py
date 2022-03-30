"""factRequestExtensionschkey

Revision ID: d53acaf848c6
Revises: e6f1bd521efc
Create Date: 2022-03-07 19:41:36.702779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd53acaf848c6'
down_revision = 'e6f1bd521efc'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('factRequestExtensions_pkey', 'factRequestExtensions', type_='primary')
    op.create_primary_key(
        "factRequestExtensions_pkey", "factRequestExtensions",
        ["requestextid","foirequestid","runcycleid"]
    )


def downgrade():
    op.drop_constraint('factRequestExtensions_pkey', 'factRequestExtensions', type_='primary')
    op.create_primary_key(
        "factRequestExtensions_pkey", "factRequestExtensions",
        ["requestextid","foirequestid","runcycleid"]
    )
