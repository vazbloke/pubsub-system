# Use an official Python runtime as a parent image
FROM postgres:latest

RUN psql -U postgres -c "create database sample;"

RUN psql -U postgres -c "create table if not exists events(event_type varchar, subscriber_email_list varchar, primary key (event_type));"

RUN psql -U postgres -c "insert into events select 'stackers','';"

RUN psql -U postgres -c "insert into events select 'fowlplay','';"

RUN psql -U postgres -c "insert into events select 'union','';"

RUN psql -U postgres -c "insert into events select 'edgyveggie','';"