FROM python:3.12-slim

WORKDIR /app
COPY todo-app.py /app/app.py

RUN useradd -u 10001 -m appuser
USER appuser

ENV PORT=8080

EXPOSE 8080
CMD ["python", "app.py"]
