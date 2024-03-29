"""update viw_analystworkloaddash to solve performance issues, aggregate divisions for each request into one column

Revision ID: bb542b1fa4cd
Revises: 8d64e381b7f5
Create Date: 2022-09-20 10:22:24.523253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb542b1fa4cd'
down_revision = '8d64e381b7f5'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""DROP VIEW public.viw_analystworkloaddash;

CREATE OR REPLACE VIEW public.viw_analystworkloaddash
 AS
 SELECT r.foirequestid,
    rd.visualrequestfilenumber AS requestid,
        CASE
            WHEN ecg.groupname::text = 'Consolidated Intake'::text THEN 'Intake'::character varying
            ELSE ecggn.groupname
        END AS team,
        CASE
            WHEN ecg.groupname::text = 'Consolidated Intake'::text THEN ecg.groupdescription
            ELSE ecggn.groupdescription
        END AS manager,
    rd.ministry,
    eco.officecode AS procorg,
    rr.requestertypeid AS category,
    rt.requesttypename AS type,
    rqt.requestertypename AS applicanttype,
    (req.lastname::text || ', '::text) || req.firstname::text AS applicantname,
    frccf.subject,
    rd.startdate,
    rd.closeddate AS enddate,
    rd.targetdate AS duedate,
    rd.processeddays AS totalprocesseddays,
    rd.currentactivity,
    frccf.currentactivitydate,
    rd.primaryusername AS analyst,
    frccf.crossgovtno,
    rd.requestdescription AS description,
    rd.status,
    frccf.customfieldstatus AS "Custom Status",
    frccf.countontime,
    frccf.countoverdue,
    frccf.onholddays,
    frccf.daysoverdue,
        CASE
            WHEN rd.requeststatus::text = 'Closed'::text THEN 'Closed'::text
            ELSE 'Not Closed'::text
        END AS notclosed,
    rpt.estimatedamount AS feesest,
    rpt.incurredamount AS feeswaived,
    rpt.paidamount AS feespaid,
    rd.disposition,
    frccf.publication,
    frccf.publicationreason,
        CASE
            WHEN rd.extension IS NULL THEN 'N'::text
            ELSE 'Y'::text
        END AS extension,
    rd.execcomments,
    frccf.noofpagesreleased AS noofpagesdelivered,
    rdd.noofpagesintherequest,
        CASE
            WHEN date_part('month'::text, rd.receiveddate) >= 4::numeric::double precision AND date_part('month'::text, rd.receiveddate) <= 12::numeric::double precision THEN COALESCE(date_part('year'::text, rd.receiveddate)::text, ''::text) || COALESCE(date_part('year'::text, rd.receiveddate + '1 year'::interval)::text, ''::text)
            WHEN date_part('month'::text, rd.receiveddate) IS NULL THEN ''::text
            ELSE COALESCE(date_part('year'::text, rd.receiveddate + '-1 years'::interval)::text, ''::text) || COALESCE(date_part('year'::text, rd.receiveddate)::text, ''::text)
        END AS startfyr,
        CASE
            WHEN date_part('month'::text, rd.closeddate) >= 4::numeric::double precision AND date_part('month'::text, rd.closeddate) <= 12::numeric::double precision THEN COALESCE(date_part('year'::text, rd.closeddate)::text, ''::text) || COALESCE(date_part('year'::text, rd.closeddate + '1 year'::interval)::text, ''::text)
            WHEN date_part('month'::text, rd.closeddate) IS NULL THEN ''::text
            ELSE COALESCE(date_part('year'::text, rd.closeddate + '-1 years'::interval)::text, ''::text) || COALESCE(date_part('year'::text, rd.closeddate)::text, ''::text)
        END AS endfyr,
        CASE
            WHEN date_part('month'::text, rd.receiveddate) >= 4::numeric::double precision AND date_part('month'::text, rd.receiveddate) <= 6::numeric::double precision THEN 1
            WHEN date_part('month'::text, rd.receiveddate) >= 7::numeric::double precision AND date_part('month'::text, rd.receiveddate) <= 9::numeric::double precision THEN 2
            WHEN date_part('month'::text, rd.receiveddate) >= 10::numeric::double precision AND date_part('month'::text, rd.receiveddate) <= 12::numeric::double precision THEN 3
            WHEN date_part('month'::text, rd.receiveddate) >= 1::numeric::double precision AND date_part('month'::text, rd.receiveddate) <= 3::numeric::double precision THEN 4
            ELSE NULL::integer
        END AS startfqtr,
        CASE
            WHEN date_part('month'::text, rd.closeddate) >= 4::numeric::double precision AND date_part('month'::text, rd.closeddate) <= 6::numeric::double precision THEN 1
            WHEN date_part('month'::text, rd.closeddate) >= 7::numeric::double precision AND date_part('month'::text, rd.closeddate) <= 9::numeric::double precision THEN 2
            WHEN date_part('month'::text, rd.closeddate) >= 10::numeric::double precision AND date_part('month'::text, rd.closeddate) <= 12::numeric::double precision THEN 3
            WHEN date_part('month'::text, rd.closeddate) >= 1::numeric::double precision AND date_part('month'::text, rd.closeddate) <= 3::numeric::double precision THEN 4
            ELSE NULL::integer
        END AS endfqtr,
    d.division,
    s.name AS stage,
        CASE
            WHEN rd.requeststatus::text = 'Closed'::text THEN 'Closed'::text
            WHEN frccf.countontime = 1 THEN 'Active'::text
            WHEN frccf.countoverdue = 1 THEN 'Overdue'::text
            ELSE NULL::text
        END AS overduestatus,
    ffrs.name AS foiflowstatus,
    ffrsd.ministryassigneefullname::character varying(250) AS assignedministryperson,
    rds2.divisions,
    rd.requeststatus,
    date_part('month'::text, rd.startdate) AS startmonth,
    rd.requesttypeid
   FROM "factRequestDetails" rd
     JOIN ( SELECT max("dimRequests".foirequestid) AS max
           FROM "dimRequests"
          GROUP BY "dimRequests".visualrequestfilenumber) foirid ON foirid.max = rd.foirequestid
     JOIN "dimRequests" r ON rd.foirequestid = r.foirequestid
     LEFT JOIN "dimECGroups" ecg ON rd.primarygroupid = ecg.groupid
     LEFT JOIN "dimECGroups" ecggn ON rd.groupname::text = ecggn.groupname::text
     LEFT JOIN "dimECOffice" eco ON rd.officeid = eco.officeid
     LEFT JOIN "dimRequestTypes" rt ON rd.requesttypeid = rt.requesttypeid
     LEFT JOIN "factRequestPaymentTransaction" rpt ON r.foirequestid = rpt.foirequestid AND rpt.activeflag = 'Y'::bpchar
     LEFT JOIN "factRequestDocumentsDetails" rdd ON r.foirequestid = rdd.foirequestid AND rdd.activeflag = 'Y'::bpchar
     LEFT JOIN "factRequestRequesters" rr ON r.foirequestid = rr.foirequestid AND rr.activeflag = 'Y'::bpchar
     LEFT JOIN "dimRequesterTypes" rqt ON rr.requestertypeid = rqt.requestertypeid
     LEFT JOIN "dimRequesters" req ON rr.requesterid = req.requesterid
     LEFT JOIN "factRequestCustomCalcFields" frccf ON rd.foirequestid = frccf.foirequestid
     LEFT JOIN ( SELECT "factRequestDivisionalStages".foirequestnumber,
            max("factRequestDivisionalStages".runcycleid) AS runcycleid,
            max("factRequestDivisionalStages".createddate) AS createddate
           FROM "factRequestDivisionalStages"
          GROUP BY "factRequestDivisionalStages".foirequestnumber) urds ON urds.foirequestnumber::text = rd.visualrequestfilenumber::text
     LEFT JOIN "factRequestDivisionalStages" rds ON rds.foirequestnumber::text = rd.visualrequestfilenumber::text AND urds.runcycleid = rds.runcycleid AND urds.createddate = rds.createddate
     LEFT JOIN "dimStages" s ON s.stageid = rds.stageid
     LEFT JOIN "dimDivisions" d ON d.divisionid = rds.divisionid
     LEFT JOIN ( SELECT "factFOIFlowRequestStatusDetails".foirequestnumber,
            max("factFOIFlowRequestStatusDetails".runcycleid) AS runcycleid,
            max("factFOIFlowRequestStatusDetails".createddate) AS createddate
           FROM "factFOIFlowRequestStatusDetails"
          GROUP BY "factFOIFlowRequestStatusDetails".foirequestnumber) uffrsd ON uffrsd.foirequestnumber::text = rd.visualrequestfilenumber::text
     LEFT JOIN "factFOIFlowRequestStatusDetails" ffrsd ON ffrsd.foirequestnumber::text = rd.visualrequestfilenumber::text AND uffrsd.runcycleid = ffrsd.runcycleid AND uffrsd.createddate = ffrsd.createddate
     LEFT JOIN "dimFOIFlowRequestStatus" ffrs ON ffrs.requeststatusid = ffrsd.requeststatusid
     LEFT JOIN ( SELECT string_agg(((('<p>'::text || d_1.division::text) || ' - '::text) || s_1.name::text) || '</p>'::text, '
'::text) AS divisions,
            rds_1.foirequestnumber
           FROM ( SELECT "factRequestDivisionalStages".foirequestnumber,
                    max("factRequestDivisionalStages".foirequestversionid) AS foirequestversionid,
                    max("factRequestDivisionalStages".runcycleid) AS runcycleid
                   FROM "factRequestDivisionalStages"
                  GROUP BY "factRequestDivisionalStages".foirequestnumber) sq
             JOIN "factRequestDivisionalStages" rds_1 ON rds_1.foirequestversionid = sq.foirequestversionid AND rds_1.runcycleid = sq.runcycleid AND rds_1.foirequestnumber::text = sq.foirequestnumber::text
             JOIN "dimStages" s_1 ON s_1.stageid = rds_1.stageid
             JOIN "dimDivisions" d_1 ON d_1.divisionid = rds_1.divisionid
          GROUP BY rds_1.foirequestnumber) rds2 ON rds2.foirequestnumber::text = rd.visualrequestfilenumber::text
  WHERE rd.activeflag = 'Y'::bpchar AND (rd.officeid <> ALL (ARRAY[1, 10, 21, 33, 41, 45, 49, 51, 55])) AND (rd.requesttypeid = ANY (ARRAY[31, 33]));

ALTER TABLE public.viw_analystworkloaddash
    OWNER TO postgres;

GRANT ALL ON TABLE public.viw_analystworkloaddash TO postgres;
GRANT SELECT ON TABLE public.viw_analystworkloaddash TO redash_role;

""")


def downgrade():
    op.execute(""" DROP VIEW public.viw_analystworkloaddash;

CREATE OR REPLACE VIEW public.viw_analystworkloaddash
 AS
 SELECT r.foirequestid,
    rd.visualrequestfilenumber AS requestid,
        CASE
            WHEN ecg.groupname::text = 'Consolidated Intake'::text THEN 'Intake'::character varying
            ELSE ecggn.groupname
        END AS team,
        CASE
            WHEN ecg.groupname::text = 'Consolidated Intake'::text THEN ecg.groupdescription
            ELSE ecggn.groupdescription
        END AS manager,
    rd.ministry,
    eco.officecode AS procorg,
    rr.requestertypeid AS category,
    rt.requesttypename AS type,
    rqt.requestertypename AS applicanttype,
    (req.lastname::text || ', '::text) || req.firstname::text AS applicantname,
    frccf.subject,
    rd.startdate,
    rd.closeddate AS enddate,
    rd.targetdate AS duedate,
    rd.processeddays AS totalprocesseddays,
    rd.currentactivity,
    frccf.currentactivitydate,
    rd.primaryusername AS analyst,
    frccf.crossgovtno,
    rd.requestdescription AS description,
    rd.status,
    frccf.customfieldstatus AS "Custom Status",
    frccf.countontime,
    frccf.countoverdue,
    frccf.onholddays,
    frccf.daysoverdue,
        CASE
            WHEN rd.requeststatus::text = 'Closed'::text THEN 'Closed'::text
            ELSE 'Not Closed'::text
        END AS notclosed,
    rpt.estimatedamount AS feesest,
    rpt.incurredamount AS feeswaived,
    rpt.paidamount AS feespaid,
    rd.disposition,
    frccf.publication,
    frccf.publicationreason,
        CASE
            WHEN rd.extension IS NULL THEN 'N'::text
            ELSE 'Y'::text
        END AS extension,
    rd.execcomments,
    frccf.noofpagesreleased AS noofpagesdelivered,
    rdd.noofpagesintherequest,
        CASE
            WHEN date_part('month'::text, rd.receiveddate) >= 4::numeric::double precision AND date_part('month'::text, rd.receiveddate) <= 12::numeric::double precision THEN COALESCE(date_part('year'::text, rd.receiveddate)::text, ''::text) || COALESCE(date_part('year'::text, rd.receiveddate + '1 year'::interval)::text, ''::text)
            WHEN date_part('month'::text, rd.receiveddate) IS NULL THEN ''::text
            ELSE COALESCE(date_part('year'::text, rd.receiveddate + '-1 years'::interval)::text, ''::text) || COALESCE(date_part('year'::text, rd.receiveddate)::text, ''::text)
        END AS startfyr,
        CASE
            WHEN date_part('month'::text, rd.closeddate) >= 4::numeric::double precision AND date_part('month'::text, rd.closeddate) <= 12::numeric::double precision THEN COALESCE(date_part('year'::text, rd.closeddate)::text, ''::text) || COALESCE(date_part('year'::text, rd.closeddate + '1 year'::interval)::text, ''::text)
            WHEN date_part('month'::text, rd.closeddate) IS NULL THEN ''::text
            ELSE COALESCE(date_part('year'::text, rd.closeddate + '-1 years'::interval)::text, ''::text) || COALESCE(date_part('year'::text, rd.closeddate)::text, ''::text)
        END AS endfyr,
        CASE
            WHEN date_part('month'::text, rd.receiveddate) >= 4::numeric::double precision AND date_part('month'::text, rd.receiveddate) <= 6::numeric::double precision THEN 1
            WHEN date_part('month'::text, rd.receiveddate) >= 7::numeric::double precision AND date_part('month'::text, rd.receiveddate) <= 9::numeric::double precision THEN 2
            WHEN date_part('month'::text, rd.receiveddate) >= 10::numeric::double precision AND date_part('month'::text, rd.receiveddate) <= 12::numeric::double precision THEN 3
            WHEN date_part('month'::text, rd.receiveddate) >= 1::numeric::double precision AND date_part('month'::text, rd.receiveddate) <= 3::numeric::double precision THEN 4
            ELSE NULL::integer
        END AS startfqtr,
        CASE
            WHEN date_part('month'::text, rd.closeddate) >= 4::numeric::double precision AND date_part('month'::text, rd.closeddate) <= 6::numeric::double precision THEN 1
            WHEN date_part('month'::text, rd.closeddate) >= 7::numeric::double precision AND date_part('month'::text, rd.closeddate) <= 9::numeric::double precision THEN 2
            WHEN date_part('month'::text, rd.closeddate) >= 10::numeric::double precision AND date_part('month'::text, rd.closeddate) <= 12::numeric::double precision THEN 3
            WHEN date_part('month'::text, rd.closeddate) >= 1::numeric::double precision AND date_part('month'::text, rd.closeddate) <= 3::numeric::double precision THEN 4
            ELSE NULL::integer
        END AS endfqtr,
    d.division,
    s.name AS stage,
        CASE
            WHEN rd.requeststatus::text = 'Closed'::text THEN 'Closed'::text
            WHEN frccf.countontime = 1 THEN 'Active'::text
            WHEN frccf.countoverdue = 1 THEN 'Overdue'::text
            ELSE NULL::text
        END AS overduestatus,
    ffrs.name AS foiflowstatus,
    ffrsd.ministryassigneefullname::character varying(250) AS assignedministryperson
   FROM "factRequestDetails" rd
     LEFT JOIN "dimRequests" r ON rd.foirequestid = r.foirequestid
     LEFT JOIN "dimECGroups" ecg ON rd.primarygroupid = ecg.groupid
     LEFT JOIN "dimECGroups" ecggn ON rd.groupname::text = ecggn.groupname::text
     LEFT JOIN "dimECOffice" eco ON rd.officeid = eco.officeid
     LEFT JOIN "dimRequestTypes" rt ON rd.requesttypeid = rt.requesttypeid
     LEFT JOIN "factRequestPaymentTransaction" rpt ON r.foirequestid = rpt.foirequestid AND rpt.activeflag = 'Y'::bpchar
     LEFT JOIN "factRequestDocumentsDetails" rdd ON r.foirequestid = rdd.foirequestid AND rdd.activeflag = 'Y'::bpchar
     LEFT JOIN "factRequestRequesters" rr ON r.foirequestid = rr.foirequestid AND rr.activeflag = 'Y'::bpchar
     LEFT JOIN "dimRequesterTypes" rqt ON rr.requestertypeid = rqt.requestertypeid
     LEFT JOIN "dimRequesters" req ON rr.requesterid = req.requesterid
     LEFT JOIN "factRequestCustomCalcFields" frccf ON rd.foirequestid = frccf.foirequestid
     LEFT JOIN ( SELECT "factRequestDivisionalStages".foirequestnumber,
            max("factRequestDivisionalStages".createddate) AS createddate
           FROM "factRequestDivisionalStages"
          GROUP BY "factRequestDivisionalStages".foirequestnumber) urds ON urds.foirequestnumber::text = rd.visualrequestfilenumber::text
     LEFT JOIN "factRequestDivisionalStages" rds ON rds.foirequestnumber::text = rd.visualrequestfilenumber::text AND urds.createddate = rds.createddate
     LEFT JOIN "dimStages" s ON s.stageid = rds.stageid
     LEFT JOIN "dimDivisions" d ON d.divisionid = rds.divisionid
     LEFT JOIN ( SELECT "factFOIFlowRequestStatusDetails".foirequestnumber,
            max("factFOIFlowRequestStatusDetails".createddate) AS createddate
           FROM "factFOIFlowRequestStatusDetails"
          GROUP BY "factFOIFlowRequestStatusDetails".foirequestnumber) uffrsd ON uffrsd.foirequestnumber::text = rd.visualrequestfilenumber::text
     LEFT JOIN "factFOIFlowRequestStatusDetails" ffrsd ON ffrsd.foirequestnumber::text = rd.visualrequestfilenumber::text AND uffrsd.createddate = ffrsd.createddate
     LEFT JOIN "dimFOIFlowRequestStatus" ffrs ON ffrs.requeststatusid = ffrsd.requeststatusid
  WHERE rd.activeflag = 'Y'::bpchar AND (eco.officecode::text <> ALL (ARRAY['IMB'::character varying::text, 'IAO'::character varying::text, 'XGR'::character varying::text, 'TIC'::character varying::text])) AND (rt.requesttypename::text = ANY (ARRAY['Consultation'::character varying::text, 'Correction'::character varying::text, 'General'::character varying::text, 'Other'::character varying::text, 'Personal'::character varying::text, 'Review'::character varying::text]));ALTER TABLE public.viw_analystworkloaddash    OWNER TO postgres;GRANT ALL ON TABLE public.viw_analystworkloaddash TO postgres;GRANT SELECT ON TABLE public.viw_analystworkloaddash TO redash_role;commit;""")

