DO $$
DECLARE
	dashboardid integer := 0;
	econdashboardid integer := 0;
	finvisualizationid integer := 0;
	econvisualizationid integer := 0;
	
	nameconcat varchar := 'FIN';
	nameecon varchar := 'ECON'	;
BEGIN
	select id into dashboardid from public.dashboards where name = CONCAT('Performance Dashboard - ', nameconcat);
	select id into econdashboardid from public.dashboards where name = CONCAT('Performance Dashboard - ', nameecon);
	
	select v.id into finvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Performance Dashboard - by Category - ', nameconcat) 
	and v.name = 'Percentage On-Time';
	
	select v.id into econvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Performance Dashboard - by Category - ', nameecon) 
	and v.name = 'Percentage On-Time';
	
	INSERT INTO public.widgets(updated_at, created_at,  visualization_id, text, width, options, dashboard_id)
 			(SELECT NOW(), NOW(), finvisualizationid as visualization_id, 
			text, width, options, dashboardid as dashboard_id 
					FROM public.widgets where dashboard_id = econdashboardid and visualization_id = econvisualizationid);
	
	select v.id into finvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Performance Dashboard - by Category - ',nameconcat) 
	and v.name = 'Total Closed';
	
	select v.id into econvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Performance Dashboard - by Category - ',nameecon) 
	and v.name = 'Total Closed';
	
	INSERT INTO public.widgets(updated_at, created_at,  visualization_id, text, width, options, dashboard_id)
 			(SELECT NOW(), NOW(), finvisualizationid as visualization_id, 
			text, width, options, dashboardid as dashboard_id 
					FROM public.widgets where dashboard_id = econdashboardid and visualization_id = econvisualizationid);
	
	select v.id into finvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Performance Dashboard - by Category - ',nameconcat) 
	and v.name = 'Average Process Days';
	
	select v.id into econvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Performance Dashboard - by Category - ',nameecon) 
	and v.name = 'Average Process Days';
	
	INSERT INTO public.widgets(updated_at, created_at,  visualization_id, text, width, options, dashboard_id)
 			(SELECT NOW(), NOW(), finvisualizationid as visualization_id, 
			text, width, options, dashboardid as dashboard_id 
					FROM public.widgets where dashboard_id = econdashboardid and visualization_id = econvisualizationid);
	
	select v.id into finvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Performance Dashboard - by Category - ',nameconcat) 
	and v.name = 'Average Days Overdue';
	
	select v.id into econvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Performance Dashboard - by Category - ',nameecon) 
	and v.name = 'Average Days Overdue';
	
	INSERT INTO public.widgets(updated_at, created_at,  visualization_id, text, width, options, dashboard_id)
 			(SELECT NOW(), NOW(), finvisualizationid as visualization_id, 
			text, width, options, dashboardid as dashboard_id 
					FROM public.widgets where dashboard_id = econdashboardid and visualization_id = econvisualizationid);
	
	select v.id into finvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Performance Dashboard - Dispositions - ',nameconcat) 
	and v.name = 'Disposition';
	
	select v.id into econvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Performance Dashboard - Dispositions - ',nameecon) 
	and v.name = 'Disposition';
	
	INSERT INTO public.widgets(updated_at, created_at,  visualization_id, text, width, options, dashboard_id)
 			(SELECT NOW(), NOW(), finvisualizationid as visualization_id, 
			text, width, options, dashboardid as dashboard_id 
					FROM public.widgets where dashboard_id = econdashboardid and visualization_id = econvisualizationid);
	
	select v.id into finvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Performance Dashboard - Details - ',nameconcat) 
	and v.name = 'Table';
	
	select v.id into econvisualizationid  from public.visualizations v 
	Inner Join public.queries q on v.query_id = q.id and q.name = CONCAT('Performance Dashboard - Details - ',nameecon) 
	and v.name = 'Table';
	
	INSERT INTO public.widgets(updated_at, created_at,  visualization_id, text, width, options, dashboard_id)
 			(SELECT NOW(), NOW(), finvisualizationid as visualization_id, 
			text, width, options, dashboardid as dashboard_id 
					FROM public.widgets where dashboard_id = econdashboardid and visualization_id = econvisualizationid);
END; $$;