psql -U postgres -c "create database sample;"

psql -U postgres -d sample -c "create table events(event_type varchar, subscriber_email_list varchar, primary key (event_type));"

psql -U postgres -d sample -c "insert into events select 'stackers','';"

psql -U postgres -d sample -c "insert into events select 'fowlplay','';"

psql -U postgres -d sample -c "insert into events select 'union','';"

psql -U postgres -d sample -c "insert into events select 'edgyveggie','';"