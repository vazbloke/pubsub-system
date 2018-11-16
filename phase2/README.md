# Phase 2

This phase implements a centralized pub-sub system.

A subscriber subscribes to a selection of four events, with their email address in the subscriber page.

The publisher publishes an message for one of the events in the publisher page.
Once published, the system notifies the subscribers of that event by email

It has two docker containers, one for the database, and one for the server.

## Database container

`docker-compose up --build`

Webpage is accessible at localhost:5000