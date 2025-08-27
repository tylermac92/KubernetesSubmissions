# syntax=docker/dockerfile:1
FROM python:3.12-slim

WORKDIR /app
COPY log_output.py /app/

# Install runtime deps
RUN pip install --no-cache-dir fastapi uvicorn

# Default port (overridable with env)
ENV PORT=8000
EXPOSE 8000

# Run the app
CMD ["sh", "-c", "uvicorn log_output:app --host 0.0.0.0 --port ${PORT}"]

