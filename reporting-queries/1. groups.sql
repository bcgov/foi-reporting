DO $$
DECLARE	
	orgid integer := 2;
	ecogroupname varchar := 'Economy Sector Group';
	fingroupname varchar := 'Finance Group';
	envgroupname varchar := 'Environment Group';
	pssggroupname varchar := 'Public Safety and Solicitor General Group';
	irrgroupname varchar := 'Indigenous Relations and Reconciliation Group';
	
BEGIN

INSERT INTO public.groups(
	org_id, type, name, permissions, created_at)
SELECT orgid, type, fingroupname, permissions, NOW() from public.groups where name = ecogroupname
UNION ALL
SELECT orgid, type, envgroupname, permissions, NOW() from public.groups where name = ecogroupname
UNION ALL
SELECT orgid, type, pssggroupname, permissions, NOW() from public.groups where name = ecogroupname
UNION ALL
SELECT orgid, type, irrgroupname, permissions, NOW() from public.groups where name = ecogroupname;

-- 	VALUES (2, 'regular', 'Finance Group', '{create_dashboard,create_query,edit_dashboard,edit_query,view_query,view_source,execute_query,list_users,schedule_query,list_dashboards,list_alerts,list_data_sources}', NOW()),
-- 			(2, 'regular', 'Environment Group', '{create_dashboard,create_query,edit_dashboard,edit_query,view_query,view_source,execute_query,list_users,schedule_query,list_dashboards,list_alerts,list_data_sources}', NOW()),
-- 			(2, 'regular', 'Public Safety and Solicitor General Group', '{create_dashboard,create_query,edit_dashboard,edit_query,view_query,view_source,execute_query,list_users,schedule_query,list_dashboards,list_alerts,list_data_sources}', NOW()),
-- 			(2, 'regular', 'Indigenous Relations and Reconciliation Group', '{create_dashboard,create_query,edit_dashboard,edit_query,view_query,view_source,execute_query,list_users,schedule_query,list_dashboards,list_alerts,list_data_sources}', NOW());

END; $$;
