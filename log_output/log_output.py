#!/usr/bin/env python3
import os
import time
import base64
import secrets
import logging
import threading
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

# Generate a single random string at startup and keep it in memory
_RANDOM_STRING = base64.b64encode(secrets.token_bytes(12)).decode("utf-8")
_LAST_LOG_TIMESTAMP = None
_LOG_INTERVAL = 5  # seconds

logging.basicConfig(level=logging.INFO, format="%(message)s")
app = FastAPI(title="Log output")

def _logger_loop():
    global _LAST_LOG_TIMESTAMP
    while True:
        _LAST_LOG_TIMESTAMP = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"[{_LAST_LOG_TIMESTAMP}] {_RANDOM_STRING}")
        time.sleep(_LOG_INTERVAL)

@app.on_event("startup")
def _start_background_logging():
    # Kick off the background logger thread
    t = threading.Thread(target=_logger_loop, daemon=True)
    t.start()
    port = int(os.getenv("PORT", "8000"))
    logging.info(f"Server started on port {port}")

@app.get("/status")
def get_status() -> JSONResponse:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload = {
        "timestamp": now,
        "random_string": _RANDOM_STRING,
        "last_log_timestamp": _LAST_LOG_TIMESTAMP,
        "interval_seconds": _LOG_INTERVAL,
    }
    return JSONResponse(content=payload)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("log_output:app", host="0.0.0.0", port=port)

