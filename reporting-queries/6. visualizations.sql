DO $$
DECLARE	

	findsid integer := 0;
	envdsid integer := 0;
	irrdsid integer := 0;
	pssgdsid integer := 0;
	
	findsname varchar := 'foiflow_edw_fin';
	envdsname varchar := 'foiflow_edw_env';
	irrdsname varchar := 'foiflow_edw_irr';
	pssgdsname varchar := 'foiflow_edw_pssg';
	
BEGIN

	SELECT id into findsid from public.data_sources where name = findsname;
	SELECT id into envdsid from public.data_sources where name = envdsname;
	SELECT id into irrdsid from public.data_sources where name = irrdsname;
	SELECT id into pssgdsid from public.data_sources where name = pssgdsname;

	INSERT INTO public.visualizations(
		updated_at, created_at,  type, query_id, name, description, options)	
	select NOW(), NOW(),  type, q.newid as query_id, v.name, description, options
	from public.visualizations v join (select sq.sname, public.queries.name, sq.id as newid, public.queries.id from public.queries 
									   inner join  
	(SELECT left(name, -6) as sname, id FROM public.queries
	where "data_source_id" = findsid
	and is_archived = false) as sq on sq.sname = public.queries.name) q  on v.query_id = q.id
	where query_id in (select id from public.queries where name in (SELECT left(name, -6) FROM public.queries
	where "data_source_id" = findsid
	and is_archived = false))

	UNION ALL

	select NOW(), NOW(),  type, q.newid as query_id, v.name, description, options
	from public.visualizations v join (select sq.sname, public.queries.name, sq.id as newid, public.queries.id from public.queries 
									   inner join  
	(SELECT left(name, -6) as sname, id FROM public.queries
	where "data_source_id" = envdsid
	and is_archived = false) as sq on sq.sname = public.queries.name) q  on v.query_id = q.id
	where query_id in (select id from public.queries where name in (SELECT left(name, -6) FROM public.queries
	where "data_source_id" = envdsid
	and is_archived = false))

	UNION ALL

	select NOW(), NOW(),  type, q.newid as query_id, v.name, description, options
	from public.visualizations v join (select sq.sname, public.queries.name, sq.id as newid, public.queries.id from public.queries 
									   inner join  
	(SELECT left(name, -6) as sname, id FROM public.queries
	where "data_source_id" = irrdsid
	and is_archived = false) as sq on sq.sname = public.queries.name) q  on v.query_id = q.id
	where query_id in (select id from public.queries where name in (SELECT left(name, -6) FROM public.queries
	where "data_source_id" = irrdsid
	and is_archived = false))

	UNION ALL

	select NOW(), NOW(),  type, q.newid as query_id, v.name, description, options
	from public.visualizations v join (select sq.sname, public.queries.name, sq.id as newid, public.queries.id from public.queries 
									   inner join  
	(SELECT left(name, -7) as sname, id FROM public.queries
	where "data_source_id" = pssgdsid
	and is_archived = false) as sq on sq.sname = public.queries.name) q  on v.query_id = q.id
	where query_id in (select id from public.queries where name in (SELECT left(name, -7) FROM public.queries
	where "data_source_id" = pssgdsid
	and is_archived = false));

END; $$;