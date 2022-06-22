-- yupdate this for options
DO $$
DECLARE	
	datarecords record;
	findsid integer := 0;
	envdsid integer := 0;
	irrdsid integer := 0;
	pssgdsid integer := 0;
	
	findsname varchar := 'foiflow_edw_fin';
	envdsname varchar := 'foiflow_edw_env';
	irrdsname varchar := 'foiflow_edw_irr';
	pssgdsname varchar := 'foiflow_edw_pssg';
	
	orgid integer := 2;
	userid integer := 2;
	
	finsubministries varchar := '''CAS'', ''LDB'', ''GCP'', ''PSA''';
	envsubministries varchar := '''EAO''';
	irrsubministries varchar := '''IRR'', ''DAS''';
	pssgsubministries varchar := '''PSS'', ''EMB'', ''OCC''';
	
	replacenamefin varchar := 'FIN';
	replacenameenv varchar := 'ENV';
	replacenameirr varchar := 'IRR';
	replacenamepssg varchar := 'PSSG';
BEGIN

	SELECT id into findsid from public.data_sources where name = findsname;
	SELECT id into envdsid from public.data_sources where name = envdsname;
	SELECT id into irrdsid from public.data_sources where name = irrdsname;
	SELECT id into pssgdsid from public.data_sources where name = pssgdsname;
	
 	INSERT INTO public.queries(
 		updated_at, created_at, version, org_id, data_source_id, latest_query_data_id, name, description, query, query_hash, api_key, 
 		user_id, last_modified_by_id, is_archived, is_draft, schedule, schedule_failures, options, search_vector, tags)
-- 	FOR datarecords IN 
	( SELECT NOW(), NOW(),  version, orgid, findsid as data_source_id,
	 latest_query_data_id, REPLACE(name, 'SAMPLE', replacenamefin) as name, description, REPLACE(query, '#sub-ministries', finsubministries) as query, query_hash, api_key, userid, last_modified_by_id, 
	 is_archived, is_draft, schedule, schedule_failures, options, search_vector, tags
			FROM public.queries where name like 'Performance%SAMPLE%'
	UNION ALL 
	SELECT NOW(), NOW(),  version, orgid, findsid as data_source_id,
	 latest_query_data_id, REPLACE(name, 'SAMPLE', replacenamefin) as name, description, REPLACE(query, '#sub-ministries', finsubministries) as query, query_hash, api_key, userid, last_modified_by_id, 
	 is_archived, is_draft, schedule, schedule_failures, options, search_vector, tags
			FROM public.queries where name like 'Received%SAMPLE%'

	UNION ALL
	SELECT NOW(), NOW(),  version, orgid, envdsid as data_source_id,
	 latest_query_data_id, REPLACE(name, 'SAMPLE', replacenameenv) as name, description, REPLACE(query, '#sub-ministries', envsubministries) as query, query_hash, api_key, userid, last_modified_by_id, 
	 is_archived, is_draft, schedule, schedule_failures, options, search_vector, tags
			FROM public.queries where name like 'Performance%SAMPLE%'
	UNION ALL 
	SELECT NOW(), NOW(),  version, orgid, envdsid as data_source_id,
	 latest_query_data_id, REPLACE(name, 'SAMPLE', replacenameenv) as name, description, REPLACE(query, '#sub-ministries', envsubministries) as query, query_hash, api_key, userid, last_modified_by_id, 
	 is_archived, is_draft, schedule, schedule_failures, options, search_vector, tags
			FROM public.queries where name like 'Received%SAMPLE%'

	UNION ALL
	SELECT NOW(), NOW(),  version, orgid, irrdsid as data_source_id,
	 latest_query_data_id, REPLACE(name, 'SAMPLE', replacenameirr) as name, description, REPLACE(query, '#sub-ministries', irrsubministries) as query, query_hash, api_key, userid, last_modified_by_id, 
	 is_archived, is_draft, schedule, schedule_failures, options, search_vector, tags
			FROM public.queries where name like 'Performance%SAMPLE%'
	UNION ALL 
	SELECT NOW(), NOW(),  version, orgid, irrdsid as data_source_id,
	 latest_query_data_id, REPLACE(name, 'SAMPLE', replacenameirr) as name, description, REPLACE(query, '#sub-ministries', irrsubministries) as query, query_hash, api_key, userid, last_modified_by_id, 
	 is_archived, is_draft, schedule, schedule_failures, options, search_vector, tags
			FROM public.queries where name like 'Received%SAMPLE%'

	UNION ALL
	SELECT NOW(), NOW(),  version, orgid, pssgdsid as data_source_id,
	 latest_query_data_id, REPLACE(name, 'SAMPLE', replacenamepssg) as name, description, REPLACE(query, '#sub-ministries', pssgsubministries) as query, query_hash, api_key, userid, last_modified_by_id, 
	 is_archived, is_draft, schedule, schedule_failures, options, search_vector, tags
			FROM public.queries where name like 'Performance%SAMPLE%'
	UNION ALL
	SELECT NOW(), NOW(),  version, orgid, pssgdsid as data_source_id,
	 latest_query_data_id, REPLACE(name, 'SAMPLE', replacenamepssg) as name, description, REPLACE(query, '#sub-ministries', pssgsubministries) as query, query_hash, api_key, userid, last_modified_by_id, 
	 is_archived, is_draft, schedule, schedule_failures, options, search_vector, tags
			FROM public.queries where name like 'Received%SAMPLE%'
	) ;
-- 	LOOP
-- 		raise notice 'name: %,  query: %', datarecords.name, datarecords.query;
-- 	END LOOP;
END; $$;