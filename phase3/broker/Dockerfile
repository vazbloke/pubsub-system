# Use python
FROM python:2.7-slim

WORKDIR /app

COPY . /app

RUN pip install requests psycopg2

# EXPOSE 80

ENV NAME World

CMD ["python", "msg_listener.py"]