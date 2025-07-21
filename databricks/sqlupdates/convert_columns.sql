%sql

CREATE TABLE your_table_new (
    foirequestid STRING,
    runcycleid STRING,
    invoiceid DOUBLE,
    invoicenumber DOUBLE,
    createdby STRING,              -- changed from DOUBLE to STRING
    createddate STRING,
    modifiedby STRING,             -- changed from DOUBLE to STRING
    modifieddate STRING,
    comments STRING,
    correspondenceid STRING,
    invoiceamount STRING,
    chargedamount STRING,
    incurredamount STRING,
    feewaived STRING,
    admincostpercentage STRING,
    chargedadmincostamount STRING,
    incurredadmincostamount DOUBLE,
    feewaivedadmincost DOUBLE,
    annotationtext STRING,
    invoiceddate TIMESTAMP,
    approvalstatus STRING,
    approvedby STRING,
    approveddate STRING,
    activeflag STRING
);

INSERT INTO your_table_new
SELECT
    foirequestid,
    runcycleid,
    invoiceid,
    invoicenumber,
    CAST(createdby AS STRING),
    createddate,
    CAST(modifiedby AS STRING),
    modifieddate,
    comments,
    correspondenceid,
    invoiceamount,
    chargedamount,
    incurredamount,
    feewaived,
    admincostpercentage,
    chargedadmincostamount,
    incurredadmincostamount,
    feewaivedadmincost,
    annotationtext,
    invoiceddate,
    approvalstatus,
    approvedby,
    approveddate,
    activeflag
FROM factrequestinvoices;

DROP TABLE factrequestinvoices;

ALTER TABLE your_table_new RENAME TO factrequestinvoices;


CREATE TABLE your_table_new (
    actionid INT,
    foirequestid INT,
    runcycleid INT,
    actiontype INT,
    description STRING,
    priority STRING,
    emailaddress STRING,
    createddate TIMESTAMP,
    actiondate TIMESTAMP,
    duedate STRING,
    responsedate STRING,
    parentactionid STRING,
    createdby STRING,
    subject STRING,
    programofficeid STRING,
    reqfordocstatusid STRING,
    completeddate STRING,
    requestofficeid INT,
    visiblerequestid STRING,
    requestdescription STRING,
    officeid INT,
    requesttypeid STRING,      -- 🟢 Changed from INT to STRING
    overduedays INT,
    elapseddays INT,
    passduedays INT,
    rfdage INT,
    remainingdays INT,
    methodofdelivery STRING,
    activeflag STRING
);

 

INSERT INTO your_table_new
SELECT
    actionid,
    foirequestid,
    runcycleid,
    actiontype,
    description,
    priority,
    emailaddress,
    createddate,
    actiondate,
    duedate,
    responsedate,
    parentactionid,
    createdby,
    subject,
    programofficeid,
    reqfordocstatusid,
    completeddate,
    requestofficeid,
    visiblerequestid,
    requestdescription,
    officeid,
    CAST(requesttypeid AS STRING),   -- 🟢 Type cast
    overduedays,
    elapseddays,
    passduedays,
    rfdage,
    remainingdays,
    methodofdelivery,
    activeflag
FROM factrequestfordocuments;

DROP TABLE factrequestfordocuments;

ALTER TABLE your_table_new RENAME TO factrequestfordocuments;