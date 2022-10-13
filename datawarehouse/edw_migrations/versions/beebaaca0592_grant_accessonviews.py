"""grant_accessonviews

Revision ID: beebaaca0592
Revises: 075395d1fbc9
Create Date: 2022-03-28 15:16:10.981174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'beebaaca0592'
down_revision = '8fb446c63f09'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('GRANT ALL ON TABLE public.viw_oipc_10_1dreport TO postgres; GRANT SELECT ON TABLE public.viw_oipc_10_1dreport TO redash_role; GRANT ALL ON TABLE public.viw_sampletlreport TO postgres; GRANT SELECT ON TABLE public.viw_sampletlreport TO redash_role;')


def downgrade():
    op.execute('GRANT ALL ON TABLE public.viw_oipc_10_1dreport TO postgres; GRANT SELECT ON TABLE public.viw_oipc_10_1dreport TO redash_role; GRANT ALL ON TABLE public.viw_sampletlreport TO postgres; GRANT SELECT ON TABLE public.viw_sampletlreport TO redash_role;')
