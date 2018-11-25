# Phase 3

This phase implements a decentralized pub-sub system.

A subscriber subscribes to a selection of four events, with their email address in the subscriber page.

This is sent to a broker at random.

The publisher publishes an message for one of the events in the publisher page.

Once published, the system notifies the subscribers of that event by email

It has five docker containers, one for the database, and one for the server, and three for the brokers.

## Build and run

`docker-compose up --build`

Webpage is accessible at localhost:5003