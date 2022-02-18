"""factRequestRedactionLayerschkey

Revision ID: 29a317713bb2
Revises: 7b2becd919ff
Create Date: 2022-02-16 16:43:10.861678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29a317713bb2'
down_revision = '7b2becd919ff'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('factRequestRedactionLayers', 'foirequestid',
               existing_type=sa.Integer(),
               nullable=True,
               schema='public')
    op.alter_column('factRequestRedactionLayers', 'docid',
               existing_type=sa.Integer(),
               nullable=False,
               schema='public')
    op.drop_constraint('factRequestRedactionLayers_foirequestid_fkey', 'factRequestRedactionLayers', type_='foreignkey')
    op.drop_constraint('factRequestRedactionLayers_pkey', 'factRequestRedactionLayers', type_='primary') 
    op.create_primary_key(
                "factRequestRedactionLayers_pkey", "factRequestRedactionLayers",
                ["redactlayerid","docid","runcycleid"]
            )


def downgrade():
    op.alter_column('factRequestRedactionLayers', 'foirequestid',
               existing_type=sa.Integer(),
               nullable=True,
               schema='public')
    op.alter_column('factRequestRedactionLayers', 'docid',
               existing_type=sa.Integer(),
               nullable=False,
               schema='public')
    op.drop_constraint('factRequestRedactionLayers_foirequestid_fkey', 'factRequestRedactionLayers', type_='foreignkey')
    op.drop_constraint('factRequestRedactionLayers_pkey', 'factRequestRedactionLayers', type_='primary') 
    op.create_primary_key(
                "factRequestRedactionLayers_pkey", "factRequestRedactionLayers",
                ["redactlayerid","docid","runcycleid"]
            )