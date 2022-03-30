*********************************************************************************************************************
Below query is used to update the developer names so that individual names do not show up as created by for a 
dashboard.

Update public.users 
set name = 'FOI Team' 
where id = 'get the id for a specific developer to update the name'

*********************************************************************************************************************
Below query is used to update the user permission on redash such that users are only able to see the dashboard link

Update public.groups 
set permissions = '{execute_query,list_dashboards}' 
where id = 'get the id for a specific group on redash to which users will be added'

*********************************************************************************************************************
Below query is used to create a user to access data from redash

CREATE ROLE role_name;
GRANT CONNECT ON DATABASE db_name TO role_name;
GRANT USAGE ON SCHEMA public TO role_name;
CREATE USER user_name WITH PASSWORD 'password';
GRANT role_name TO user_name;