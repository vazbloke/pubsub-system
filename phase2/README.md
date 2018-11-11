# Phase 2

This phase implements a centralized pub-sub system.

A subscriber subscribes to a selection of four events, with their email address in the subscriber page.

The publisher publishes an message for one of the events in the publisher page.
Once published, the system notifies the subscribers of that event by email

It has two docker containers, one for the database, and one for the server.

## Database container

`docker run -d -p 5432:5432 --name my-postgres -e POSTGRES_PASSWORD=root postgres`

`docker exec -it my-postgres bash`

`psql -U postgres`

`create database sample;`

`\c sample;`

`create table events(event_type varchar, subscriber_email_list varchar, primary key (event_type));`

`insert into events select 'stackers','';`
`insert into events select 'fowlplay','';`
`insert into events select 'union','';`
`insert into events select 'edgyveggie','';`

### Get DB container's IP (New terminal)

`docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-postgres`

Replace "HOST" in db.py with IP returned from command

## Server container

`docker build -t phase2 .`

`docker run -d -p 5000:80 phase2`

Webpage is accessible at localhost:5000