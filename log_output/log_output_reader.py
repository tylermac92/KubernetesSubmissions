#!/usr/bin/env python3
import os
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
import uvicorn

LOG_PATH = Path(os.getenv("LOG_PATH", "/data/log.txt"))
PORT = int(os.getenv("PORT", "8000"))

app = FastAPI(title="Log output (reader)")

def read_last_line(path: Path) -> str:
    if not path.exists():
        return ""
    # Efficient last-line read for reasonably sized files
    with path.open("rb") as f:
        try:
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b"\n":
                f.seek(-2, os.SEEK_CUR)
        except OSError:
            f.seek(0)
        last = f.readline().decode("utf-8", errors="replace").rstrip("\n")
    return last

@app.get("/status")
def status() -> JSONResponse:
    last = read_last_line(LOG_PATH)
    if not last:
        # No content yet; still startable
        return JSONResponse({"last_line": None, "message": "No log entries yet."})
    return JSONResponse({"last_line": last})

# Optional: plain-text for quick curl checks
@app.get("/")
def root() -> PlainTextResponse:
    last = read_last_line(LOG_PATH) or "No log entries yet."
    return PlainTextResponse(last)

if __name__ == "__main__":
    uvicorn.run("log_output_reader:app", host="0.0.0.0", port=PORT)

