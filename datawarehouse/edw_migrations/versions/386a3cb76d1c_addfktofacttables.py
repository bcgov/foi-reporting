"""addFKtofacttables

Revision ID: 386a3cb76d1c
Revises: 4e6e81886c50
Create Date: 2022-01-27 12:31:49.211456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '386a3cb76d1c'
down_revision = '4e6e81886c50'
branch_labels = None
depends_on = None


def upgrade():
	op.create_foreign_key(None, 'factRequestPaymentTransaction', 'dimRunCycle', ['runcycleid'], ['runcycleid'])  
	op.create_foreign_key(None, 'factRequestPaymentTransaction', 'dimRequests', ['foirequestid'], ['foirequestid'])
	op.create_foreign_key(None, 'factRequestExtensions', 'dimRunCycle', ['runcycleid'], ['runcycleid'])  
	op.create_foreign_key(None, 'factRequestExtensions', 'dimRequests', ['foirequestid'], ['foirequestid'])
	op.create_foreign_key(None, 'factRequestForDocuments', 'dimRunCycle', ['runcycleid'], ['runcycleid'])  
	op.create_foreign_key(None, 'factRequestForDocuments', 'dimRequests', ['foirequestid'], ['foirequestid'])
	op.create_foreign_key(None, 'factRequestForDocuments', 'dimProgramOffices', ['programofficeid'], ['programofficeid'])
	op.create_foreign_key(None, 'factRequestRequesters', 'dimRunCycle', ['runcycleid'], ['runcycleid'])  
	op.create_foreign_key(None, 'factRequestRequesters', 'dimRequests', ['foirequestid'], ['foirequestid'])


def downgrade():
	op.create_foreign_key(None, 'factRequestPaymentTransaction', 'dimRunCycle', ['runcycleid'], ['runcycleid'])  
	op.create_foreign_key(None, 'factRequestPaymentTransaction', 'dimRequests', ['foirequestid'], ['foirequestid'])
	op.create_foreign_key(None, 'factRequestExtensions', 'dimRunCycle', ['runcycleid'], ['runcycleid'])  
	op.create_foreign_key(None, 'factRequestExtensions', 'dimRequests', ['foirequestid'], ['foirequestid'])
	op.create_foreign_key(None, 'factRequestForDocuments', 'dimRunCycle', ['runcycleid'], ['runcycleid'])  
	op.create_foreign_key(None, 'factRequestForDocuments', 'dimRequests', ['foirequestid'], ['foirequestid'])
	op.create_foreign_key(None, 'factRequestForDocuments', 'dimProgramOffices', ['programofficeid'], ['programofficeid'])
	op.create_foreign_key(None, 'factRequestRequesters', 'dimRunCycle', ['runcycleid'], ['runcycleid'])  
	op.create_foreign_key(None, 'factRequestRequesters', 'dimRequests', ['foirequestid'], ['foirequestid'])
