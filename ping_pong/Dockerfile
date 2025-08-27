# syntax=docker/dockerfile:1
FROM python:3.12-slim

WORKDIR /app
COPY ping_pong.py /app/

RUN pip install --no-cache-dir fastapi uvicorn

ENV PORT=9000
EXPOSE 9000

CMD ["sh", "-c", "uvicorn ping_pong:app --host 0.0.0.0 --port ${PORT}"]

