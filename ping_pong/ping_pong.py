#!/usr/bin/env python3
import os
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn

app = FastAPI(title="Ping Pong Application")

# In-memory counter
counter = 0

@app.get("/pingpong")
def pingpong() -> PlainTextResponse:
    global counter
    response = f"pong {counter}"
    counter += 1
    return PlainTextResponse(response)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "9000"))
    uvicorn.run("ping_pong:app", host="0.0.0.0", port=port)

