# Use python
FROM python:3.7.1-slim

WORKDIR /app

COPY . /app

RUN pip install requests psycopg2-binary

# RUN chmod +x wait-for-it.sh

# EXPOSE 80

ENV NAME World

CMD ["python", "-u", "msg_listener.py"]
# CMD ["./wait-for-it.sh", "my-postgres-db", "python", "msg_listener.py"]