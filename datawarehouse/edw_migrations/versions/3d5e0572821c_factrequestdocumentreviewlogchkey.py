"""factRequestDocumentReviewLogchkey

Revision ID: 3d5e0572821c
Revises: 29a317713bb2
Create Date: 2022-02-16 16:43:58.309405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d5e0572821c'
down_revision = '29a317713bb2'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('factRequestDocumentReviewLog_pkey', 'factRequestDocumentReviewLog', type_='primary') 
    op.create_primary_key(
                "factRequestDocumentReviewLog_pkey", "factRequestDocumentReviewLog",
                ["docid","foirequestid","runcycleid"]
            )


def downgrade():
    op.drop_constraint('factRequestDocumentReviewLog_pkey', 'factRequestDocumentReviewLog', type_='primary') 
    op.create_primary_key(
                "factRequestDocumentReviewLog_pkey", "factRequestDocumentReviewLog",
                ["docid"],["foirequestid"],["runcycleid"]
            )