DO $$
DECLARE	
	orgid integer := 2;
	findsname varchar := 'foiflow_edw_fin';
	envdsname varchar := 'foiflow_edw_env';
	irrdsname varchar := 'foiflow_edw_irr';
	pssgdsname varchar := 'foiflow_edw_pssg';
	econdsname varchar := 'foiflow_edw_econ';
BEGIN

	INSERT INTO public.data_sources(
		org_id, name, type, encrypted_options, queue_name, scheduled_queue_name, created_at)
		(SELECT orgid, findsname, type, encrypted_options, queue_name, scheduled_queue_name, NOW()
		FROM public.data_sources where name = econdsname)
		UNION ALL
		(SELECT orgid, envdsname, type, encrypted_options, queue_name, scheduled_queue_name, NOW()
		FROM public.data_sources where name = econdsname)
		UNION ALL
		(SELECT orgid, irrdsname, type, encrypted_options, queue_name, scheduled_queue_name, NOW()
		FROM public.data_sources where name = econdsname)
		UNION ALL
		(SELECT orgid, pssgdsname, type, encrypted_options, queue_name, scheduled_queue_name, NOW()
		FROM public.data_sources where name = econdsname);
END; $$;