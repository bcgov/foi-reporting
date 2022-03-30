"""viw_analystworkloaddash

Revision ID: 5397f07013f3
Revises: 78308d02957d
Create Date: 2022-02-28 20:04:01.077049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5397f07013f3'
down_revision = '78308d02957d'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE OR REPLACE VIEW viw_analystworkloaddash AS Select R.foirequestid as foirequestid, R.visualrequestfilenumber as requestid, case when ECG.groupname = \'Consolidated Intake\' then \'Intake\' else ECGGN.groupname end as team, case when ECG.groupname = \'Consolidated Intake\' then ECG.groupdescription else ECGGN.groupdescription end as manager, RD.ministry, ECO.officecode as procorg, RD.applicantcategoryid as category, RT.requesttypename as type, RQT.requestertypename as applicanttype, REQ.lastname || \', \' || REQ.firstname as applicantname, RD.subject, RD.startdate, RD.closeddate as enddate, RD.targetdate as duedate, RD.processeddays as totalprocesseddays, RD.currentactivity, RD.currentactivitydate, RD.primaryusername as analyst, RD.crossgovtno, RD.requestdescription as description, RD.status as status, RD.countontime, RD.countoverdue, RD.onholddays, RD.daysoverdue, case when RD.requeststatus = \'Closed\' then \'Closed\' else \'Not Closed\' end as notclosed, RPT.estimatedamount as feesest, RPT.incurredamount as feeswaived, RPT.paidamount as feespaid, RD.disposition, RD.publication, RD.publicationreason, case when RD.extension is null then \'N\' else \'Y\' end as extension, RD.execcomments, RDD.noofpagesreleased as noofpagesdelivered, RDD.noofpagesintherequest, CASE WHEN EXTRACT(MONTH FROM RD.receiveddate) BETWEEN 4 AND 12 THEN COALESCE(EXTRACT(YEAR FROM RD.receiveddate)::TEXT , \'\') || COALESCE(EXTRACT(YEAR FROM (RD.receiveddate + INTERVAL \'12 month\'))::TEXT,\'\') WHEN EXTRACT(MONTH FROM RD.receiveddate) is null THEN \'\'  ELSE COALESCE(EXTRACT(YEAR FROM (RD.receiveddate + INTERVAL \'-12 month\'))::TEXT , \'\') || COALESCE(EXTRACT(YEAR FROM RD.receiveddate)::TEXT , \'\') END as startfyr, CASE  WHEN EXTRACT(MONTH FROM RD.closeddate) BETWEEN 4 AND 12 THEN COALESCE(EXTRACT(YEAR FROM RD.closeddate)::TEXT , \'\') || COALESCE(EXTRACT(YEAR FROM (RD.closeddate + INTERVAL \'12 month\'))::TEXT,\'\') WHEN EXTRACT(MONTH FROM RD.closeddate) is null THEN \'\'  ELSE COALESCE(EXTRACT(YEAR FROM (RD.closeddate + INTERVAL \'-12 month\'))::TEXT , \'\') || COALESCE(EXTRACT(YEAR FROM RD.closeddate)::TEXT , \'\') END as endfyr, CASE WHEN EXTRACT(MONTH FROM RD.receiveddate) BETWEEN 4 AND 6 THEN 1 WHEN EXTRACT(MONTH FROM RD.receiveddate) BETWEEN 7 AND 9 THEN 2 WHEN EXTRACT(MONTH FROM RD.receiveddate) BETWEEN 10 AND 12 THEN 3 WHEN EXTRACT(MONTH FROM RD.receiveddate) BETWEEN 1 AND 3 THEN 4 END as startfqtr, CASE WHEN EXTRACT(MONTH FROM RD.closeddate) BETWEEN 4 AND 6 THEN 1 WHEN EXTRACT(MONTH FROM RD.closeddate) BETWEEN 7 AND 9 THEN 2 WHEN EXTRACT(MONTH FROM RD.closeddate) BETWEEN 10 AND 12 THEN 3 WHEN EXTRACT(MONTH FROM RD.closeddate) BETWEEN 1 AND 3 THEN 4 END as endfqtr from public."factRequestDetails" RD left outer join public."dimRequests" R on RD.foirequestid = R.foirequestid left outer join public."dimECGroups" ECG on RD.primarygroupid = ECG.groupid left outer join public."dimECGroups" ECGGN on RD.groupname = ECGGN.groupname left outer join public."dimECOffice" ECO on RD.officeid = ECO.officeid left outer join public."dimRequestTypes" RT on RD.requesttypeid = RT.requesttypeid left outer join public."dimRequesterTypes" RQT on RD.applicantcategoryid = RQT.requestertypeid left outer join public."factRequestPaymentTransaction" RPT on R.foirequestid = RPT.foirequestid and RPT.activeflag = \'Y\' left outer join public."factRequestDocumentsDetails" RDD on R.foirequestid = RDD.foirequestid and RDD.activeflag = \'Y\' left outer join public."factRequestRequesters" RR on R.foirequestid = RR.foirequestid and RR.activeflag = \'Y\' left outer join public."dimRequesters" REQ on RR.requesterid = REQ.requesterid WHERE rd.activeflag = \'Y\' and ECO.officecode not in (\'IMB\',\'IAO\',\'XGR\') AND RT.requesttypename IN (\'Consultation\', \'Correction\', \'General\', \'Other\', \'Personal\', \'Review\');commit;')


def downgrade():
    op.drop_view(viw_analystworkloaddash)
