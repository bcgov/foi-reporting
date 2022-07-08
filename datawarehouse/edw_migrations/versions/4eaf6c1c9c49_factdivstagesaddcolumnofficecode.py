"""empty message

Revision ID: 4eaf6c1c9c49
Revises: 054e7c836ebd
Create Date: 2022-07-07 22:42:33.656931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4eaf6c1c9c49'
down_revision = '054e7c836ebd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('factRequestDivisionalStages', sa.Column('officecode', sa.VARCHAR(length=50), nullable=False))    
    op.drop_column('factRequestDivisionalStages', 'officeid')


def downgrade():
    op.add_column('factRequestDivisionalStages', sa.Column('officeid', sa.Integer(), nullable=False))
    op.drop_column('factRequestDivisionalStages', 'officecode')	
