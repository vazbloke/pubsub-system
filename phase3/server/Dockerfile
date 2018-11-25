# Use python
FROM python:3.7.1-slim

WORKDIR /app

COPY . /app

RUN pip install Flask requests psycopg2-binary

EXPOSE 80

ENV NAME World

CMD ["python", "-u", "server.py"]