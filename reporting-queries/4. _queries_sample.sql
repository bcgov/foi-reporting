DO $$
DECLARE	
	query_texts record;
	orgid integer := 2;
	userid integer := 2;
BEGIN
	
 	--FOR query_texts IN (SELECT query, name FROM public.queries where name like 'Performance%ECON%') LOOP
 	INSERT INTO public.queries(
 		updated_at, created_at, version, org_id, data_source_id, latest_query_data_id, name, description, query, query_hash, api_key, 
 		user_id, last_modified_by_id, is_archived, is_draft, schedule, schedule_failures, options, search_vector, tags)
 		SELECT NOW(), NOW(), 1, orgid, data_source_id, latest_query_data_id, REPLACE(name, 'ECON', 'SAMPLE'), '', 
 		REPLACE(query, '''JER'', ''LBR'', ''TAC'', ''MMA''','#sub-ministries'), query_hash, api_key, userid, last_modified_by_id, 
 	 is_archived, is_draft, schedule, schedule_failures, options, search_vector, tags from public.queries where name like 'Performance%ECON%';
 	--END LOOP;
	--FOR query_texts IN (SELECT query, name FROM public.queries where name like 'Received%ECON%') LOOP
	INSERT INTO public.queries(
		updated_at, created_at, version, org_id, data_source_id, latest_query_data_id, name, description, query, query_hash, api_key, 
		user_id, last_modified_by_id, is_archived, is_draft, schedule, schedule_failures, options, search_vector, tags)
		SELECT NOW(), NOW(), 1, orgid, data_source_id, latest_query_data_id, REPLACE(name, 'ECON', 'SAMPLE'), '', 
		REPLACE(query, '''JER'', ''LBR'', ''TAC'', ''MMA''','#sub-ministries'), query_hash, api_key, userid, last_modified_by_id, 
	 is_archived, is_draft, schedule, schedule_failures, options, search_vector, tags from public.queries where name like 'Received%ECON%';
	--END LOOP;
	
END; $$;