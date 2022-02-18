"""factRequestExtensionschgkey

Revision ID: 1cc0deead1b9
Revises: b755861e3f93
Create Date: 2022-02-16 16:46:13.580378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cc0deead1b9'
down_revision = 'b755861e3f93'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('factRequestExtensions', sa.Column('requestextid', sa.Integer(), nullable=False))
    op.drop_constraint('factRequestExtensions_pkey', 'factRequestExtensions', type_='primary') 
    op.create_primary_key(
                "factRequestExtensions_pkey", "factRequestExtensions",
                ["requestextid"]
            )


def downgrade():
    op.add_column('factRequestExtensions', sa.Column('requestextid', sa.Integer(), nullable=False))
    op.drop_constraint('factRequestExtensions_pkey', 'factRequestExtensions', type_='primary') 
    op.create_primary_key(
                "factRequestExtensions_pkey", "factRequestExtensions",
                ["requestextid"]
            )