%sql

%sql

alter table dimaddress ADD COLUMNS (
    sourceoftruth string
);
update dimaddress set sourceoftruth = 'AXIS';

alter table dimdeliverymodes ADD COLUMNS (
    sourceoftruth string
);
update dimdeliverymodes set sourceoftruth = 'AXIS';

alter table dimdivisions ADD COLUMNS (
    sourceoftruth string
);
update dimdivisions set sourceoftruth = 'AXIS';

alter table dimecgroups ADD COLUMNS (
    sourceoftruth string
);
update dimecgroups set sourceoftruth = 'AXIS';

alter table dimextensiontypes ADD COLUMNS (
    sourceoftruth string
);
update dimextensiontypes set sourceoftruth = 'AXIS';

alter table dimfoiflowrequeststatus ADD COLUMNS (
    sourceoftruth string
);
update dimfoiflowrequeststatus set sourceoftruth = 'AXIS';

alter table diminvoicedetails ADD COLUMNS (
    sourceoftruth string
);
update diminvoicedetails set sourceoftruth = 'AXIS';

alter table dimmodministryrequestids ADD COLUMNS (
    sourceoftruth string
);
update dimmodministryrequestids set sourceoftruth = 'AXIS';

alter table dimmodpageflags ADD COLUMNS (
    sourceoftruth string
);
update dimmodpageflags set sourceoftruth = 'AXIS';

alter table dimreceivedmodes ADD COLUMNS (
    sourceoftruth string
);
update dimreceivedmodes set sourceoftruth = 'AXIS';

alter table dimrequestertypes ADD COLUMNS (
    sourceoftruth string
);
update dimrequestertypes set sourceoftruth = 'AXIS';

alter table dimrequestfordocumentsstatus ADD COLUMNS (
    sourceoftruth string
);
update dimrequestfordocumentsstatus set sourceoftruth = 'AXIS';

alter table dimrequeststatuses ADD COLUMNS (
    sourceoftruth string
);
update dimrequeststatuses set sourceoftruth = 'AXIS';

alter table dimstages ADD COLUMNS (
    sourceoftruth string
);
update dimstages set sourceoftruth = 'AXIS';

alter table factrequestcustomcalcfields ADD COLUMNS (
    sourceoftruth string
);

update factrequestcustomcalcfields set sourceoftruth = 'AXIS';

alter table factRequestExtensions ADD COLUMNS (
    sourceoftruth string
);

update factRequestExtensions set sourceoftruth = 'AXIS';

alter table factrequestfordocuments ADD COLUMNS (
    sourceoftruth string
);

update factrequestfordocuments set sourceoftruth = 'AXIS';

alter table factrequestpaymenttransaction ADD COLUMNS (
    sourceoftruth string
);

update factrequestpaymenttransaction set sourceoftruth = 'AXIS';

alter table factrequestinvoices ADD COLUMNS (
    sourceoftruth string
);

update factrequestinvoices set sourceoftruth = 'AXIS';

alter table factrequestdetails ADD COLUMNS (
    sourceoftruth string
);

update factrequestdetails set sourceoftruth = 'AXIS';

alter table factrequestoipcfields ADD COLUMNS (
    sourceoftruth string
);

update factrequestoipcfields set sourceoftruth = 'AXIS';

alter table factrequestrequesters ADD COLUMNS (
    sourceoftruth string
);

update factrequestrequesters set sourceoftruth = 'AXIS';



