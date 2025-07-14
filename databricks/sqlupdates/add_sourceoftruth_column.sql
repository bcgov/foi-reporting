%sql

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



