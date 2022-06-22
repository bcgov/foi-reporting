DO $$
DECLARE
	dashboardid integer := 0;
	econdashboardid integer := 0;
	visualizationid integer := 0;
	econvisualizationid integer := 0;
	
	nameconcat varchar := 'ENV';
	
BEGIN
	select id into dashboardid from public.dashboards where name = CONCAT('Received Dashboard - ', nameconcat);
	select id into econdashboardid from public.dashboards where name = 'Received Dashboard';
	
	select v.id into visualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Received Dashboard - Total Received - ', nameconcat) and v.type = 'COUNTER';
	
	select v.id into econvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = 'Received Dashboard - Total Received' and v.type = 'COUNTER' ;
	
	INSERT INTO public.widgets(updated_at, created_at,  visualization_id, text, width, options, dashboard_id)
 			(SELECT NOW(), NOW(), visualizationid as visualization_id, 
			text, width, options, dashboardid as dashboard_id 
					FROM public.widgets where dashboard_id = econdashboardid and visualization_id = econvisualizationid);
	
	select v.id into visualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Received Dashboard - Total Received by Time Period - ', nameconcat) and v.type = 'CHART' ;
	
	select v.id into econvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = 'Received Dashboard - Total Received by Time Period' and v.type = 'CHART' ;
	
	INSERT INTO public.widgets(updated_at, created_at,  visualization_id, text, width, options, dashboard_id)
 			(SELECT NOW(), NOW(), visualizationid as visualization_id, 
			text, width, options, dashboardid as dashboard_id 
					FROM public.widgets where dashboard_id = econdashboardid and visualization_id = econvisualizationid);
	
	select v.id into visualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Received Dashboard - Total Received by ProcORG - ', nameconcat) and v.type = 'CHART' ;
	
	select v.id into econvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = 'Received Dashboard - Total Received by ProcORG' and v.type = 'CHART' ;
	
	INSERT INTO public.widgets(updated_at, created_at,  visualization_id, text, width, options, dashboard_id)
 			(SELECT NOW(), NOW(), visualizationid as visualization_id, 
			text, width, options, dashboardid as dashboard_id 
					FROM public.widgets where dashboard_id = econdashboardid and visualization_id = econvisualizationid);
	
	select v.id into visualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Received Dashboard - Total Received by Applicant Type - ', nameconcat) and v.type = 'CHART' ;
	
	select v.id into econvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = 'Received Dashboard - Total Received by Applicant Type' and v.type = 'CHART' ;
	
	INSERT INTO public.widgets(updated_at, created_at,  visualization_id, text, width, options, dashboard_id)
 			(SELECT NOW(), NOW(), visualizationid as visualization_id, 
			text, width, options, dashboardid as dashboard_id 
					FROM public.widgets where dashboard_id = econdashboardid and visualization_id = econvisualizationid);
	
	select v.id into visualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Received Dashboard - Total Active by ProcORG - ', nameconcat) and v.type = 'CHART' ;
	
	select v.id into econvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = 'Received Dashboard - Total Active by ProcORG' and v.type = 'CHART' ;
	
	INSERT INTO public.widgets(updated_at, created_at,  visualization_id, text, width, options, dashboard_id)
 			(SELECT NOW(), NOW(), visualizationid as visualization_id, 
			text, width, options, dashboardid as dashboard_id 
					FROM public.widgets where dashboard_id = econdashboardid and visualization_id = econvisualizationid);
	
	select v.id into visualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Received Dashboard - Total Active by ApplicantType - ', nameconcat) and v.type = 'CHART' ;
	
	select v.id into econvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = 'Received Dashboard - Total Active by ApplicantType' and v.type = 'CHART' ;
	
	INSERT INTO public.widgets(updated_at, created_at,  visualization_id, text, width, options, dashboard_id)
 			(SELECT NOW(), NOW(), visualizationid as visualization_id, 
			text, width, options, dashboardid as dashboard_id 
					FROM public.widgets where dashboard_id = econdashboardid and visualization_id = econvisualizationid);
	
	select v.id into visualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Received Dashboard - Total Active by Status - ', nameconcat) and v.type = 'CHART' ;
	
	select v.id into econvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = 'Received Dashboard - Total Active by Status' and v.type = 'CHART' ;
	
	INSERT INTO public.widgets(updated_at, created_at,  visualization_id, text, width, options, dashboard_id)
 			(SELECT NOW(), NOW(), visualizationid as visualization_id, 
			text, width, options, dashboardid as dashboard_id 
					FROM public.widgets where dashboard_id = econdashboardid and visualization_id = econvisualizationid);
	
	select v.id into visualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Received Dashboard - Total Active by On-Time/Overdue - ', nameconcat) and v.type = 'CHART' ;
	
	select v.id into econvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = 'Received Dashboard - Total Active by On-Time/Overdue' and v.type = 'CHART' ;
	
	INSERT INTO public.widgets(updated_at, created_at,  visualization_id, text, width, options, dashboard_id)
 			(SELECT NOW(), NOW(), visualizationid as visualization_id, 
			text, width, options, dashboardid as dashboard_id 
					FROM public.widgets where dashboard_id = econdashboardid and visualization_id = econvisualizationid);
	
	select v.id into visualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Received Dashboard - Total Active by CurrentActivity - ', nameconcat) and v.type = 'CHART' ;
	
	select v.id into econvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = 'Received Dashboard - Total Active by CurrentActivity' and v.type = 'CHART' ;
	
	INSERT INTO public.widgets(updated_at, created_at,  visualization_id, text, width, options, dashboard_id)
 			(SELECT NOW(), NOW(), visualizationid as visualization_id, 
			text, width, options, dashboardid as dashboard_id 
					FROM public.widgets where dashboard_id = econdashboardid and visualization_id = econvisualizationid);
	
	select v.id into visualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Received Dashboard - Details - ', nameconcat) and v.type = 'TABLE' ;
	
	select v.id into econvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = 'Received Dashboard - Details' and v.type = 'TABLE' ;
	
	INSERT INTO public.widgets(updated_at, created_at,  visualization_id, text, width, options, dashboard_id)
 			(SELECT NOW(), NOW(), visualizationid as visualization_id, 
			text, width, options, dashboardid as dashboard_id 
					FROM public.widgets where dashboard_id = econdashboardid and visualization_id = econvisualizationid);
END; $$;