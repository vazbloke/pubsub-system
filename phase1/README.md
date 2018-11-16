# Phase 1

This phase implements a python code executor, where input is Python code and the output is displayed.

## Build and run container

`docker build -t phase1 .`

`docker run --name my-server -d -p 4000:80 phase1`

Webpage is accessible at localhost:4000