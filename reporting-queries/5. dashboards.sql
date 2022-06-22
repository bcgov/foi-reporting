DO $$
DECLARE	
	orgid integer := 2;
	userid integer := 2;
	
	replacenamefin varchar := 'FIN';
	replacenameenv varchar := 'ENV';
	replacenameirr varchar := 'IRR';
	replacenamepssg varchar := 'PSSG';
	econname varchar := 'ECON';
	
BEGIN

	INSERT INTO public.dashboards(
		updated_at, created_at, version, org_id, slug, name, user_id, layout, dashboard_filters_enabled, is_archived, is_draft, tags, options)
		(
		SELECT NOW(), NOW(), version, orgid, REPLACE(slug, LOWER(econname), LOWER(replacenamefin)) as slug, REPLACE(name, econname, replacenamefin) as name, userid, layout, dashboard_filters_enabled, is_archived, 
		is_draft, tags, options
			FROM public.dashboards where name like 'Performance%ECON'
		UNION ALL	
		SELECT NOW(), NOW(), version, orgid, REPLACE(slug, LOWER(econname), LOWER(replacenamefin)) as slug, REPLACE(name, econname, replacenamefin) as name, userid, layout, dashboard_filters_enabled, is_archived, 
		is_draft, tags, options
			FROM public.dashboards where name like 'Received%ECON'
		UNION ALL
		SELECT NOW(), NOW(), version, orgid, REPLACE(slug, LOWER(econname), LOWER(replacenameenv)) as slug, REPLACE(name, econname, replacenameenv) as name, userid, layout, dashboard_filters_enabled, is_archived, 
		is_draft, tags, options
			FROM public.dashboards where name like 'Performance%ECON'
		UNION ALL	
		SELECT NOW(), NOW(), version, orgid, REPLACE(slug, LOWER(econname), LOWER(replacenameenv)) as slug, REPLACE(name, econname, replacenameenv) as name, userid, layout, dashboard_filters_enabled, is_archived, 
		is_draft, tags, options
			FROM public.dashboards where name like 'Received%ECON'
		UNION ALL
		SELECT NOW(), NOW(), version, orgid, REPLACE(slug, LOWER(econname), LOWER(replacenameirr)) as slug, REPLACE(name, econname, replacenameirr) as name, userid, layout, dashboard_filters_enabled, is_archived, 
		is_draft, tags, options
			FROM public.dashboards where name like 'Performance%ECON'
		UNION ALL	
		SELECT NOW(), NOW(), version, orgid, REPLACE(slug, LOWER(econname), LOWER(replacenameirr)) as slug, REPLACE(name, econname, replacenameirr) as name, userid, layout, dashboard_filters_enabled, is_archived, 
		is_draft, tags, options
			FROM public.dashboards where name like 'Received%ECON'
		UNION ALL
		SELECT NOW(), NOW(), version, orgid, REPLACE(slug, LOWER(econname), LOWER(replacenamepssg)) as slug, REPLACE(name, econname, replacenamepssg) as name, userid, layout, dashboard_filters_enabled, is_archived, 
		is_draft, tags, options
			FROM public.dashboards where name like 'Performance%ECON'
		UNION ALL	
		SELECT NOW(), NOW(), version, orgid, REPLACE(slug, LOWER(econname), LOWER(replacenamepssg)) as slug, REPLACE(name, econname, replacenamepssg) as name, userid, layout, dashboard_filters_enabled, is_archived, 
		is_draft, tags, options
			FROM public.dashboards where name like 'Received%ECON'
		);
END; $$;