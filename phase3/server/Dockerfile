# Use python
FROM python:2.7-slim

WORKDIR /app

COPY . /app

RUN pip install Flask requests psycopg2-binary

EXPOSE 80

ENV NAME World

CMD ["python", "server.py"]