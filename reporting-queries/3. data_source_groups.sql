DO $$
DECLARE	
	findsid integer := 0;
	envdsid integer := 0;
	irrdsid integer := 0;
	pssgdsid integer := 0;
	
	fingroupid integer := 0;
	envgroupid integer := 0;
	irrgroupid integer := 0;
	pssggroupid integer := 0;
	
	findsname varchar := 'foiflow_edw_fin';
	envdsname varchar := 'foiflow_edw_env';
	irrdsname varchar := 'foiflow_edw_irr';
	pssgdsname varchar := 'foiflow_edw_pssg';

	fingroupname varchar := 'Finance Group';
	envgroupname varchar := 'Environment Group';
	pssggroupname varchar := 'Public Safety and Solicitor General Group';
	irrgroupname varchar := 'Indigenous Relations and Reconciliation Group';
	
BEGIN

	SELECT id into findsid from public.data_sources where name = findsname;
	SELECT id into envdsid from public.data_sources where name = envdsname;
	SELECT id into irrdsid from public.data_sources where name = irrdsname;
	SELECT id into pssgdsid from public.data_sources where name = pssgdsname;
	
	SELECT id into fingroupid from public.groups where name = fingroupname;
	SELECT id into envgroupid from public.groups where name = envgroupname;
	SELECT id into irrgroupid from public.groups where name = irrgroupname;
	SELECT id into pssggroupid from public.groups where name = pssggroupname;
	

	INSERT INTO public.data_source_groups(
		data_source_id, group_id, view_only)
		VALUES (findsid, fingroupid, True),
	(envdsid, envgroupid, True),
	(irrdsid, irrgroupid, True),
	(pssgdsid, pssggroupid, True);
	
END; $$;
	




