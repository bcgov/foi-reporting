"""empty message

Revision ID: 058a4f62843d
Revises: None
Create Date: 2022-03-23 15:39:09.131579

"""
from alembic import op
import sqlalchemy as sa
import os


# revision identifiers, used by Alembic.
revision = '058a4f62843d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE ROLE redash_role; '  \
'GRANT CONNECT ON DATABASE foi_edw TO redash_role; '\
'GRANT USAGE ON SCHEMA public TO redash_role; '\
'CREATE USER redash_user WITH PASSWORD \''+ os.getenv('redash_user_password') +'\';'\
'GRANT redash_role TO redash_user;')


def downgrade():
    pass
