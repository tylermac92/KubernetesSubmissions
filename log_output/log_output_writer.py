#!/usr/bin/env python3
import os
import time
import base64
import secrets
from datetime import datetime
from pathlib import Path

LOG_PATH = Path(os.getenv("LOG_PATH", "/data/log.txt"))
INTERVAL = int(os.getenv("INTERVAL", "5"))

def main():
    # Ensure dir exists
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    # One random string for the lifetime of the container
    rnd = base64.b64encode(secrets.token_bytes(12)).decode("utf-8")
    port = os.getenv("PORT", "8000")  # not used, but mirrored from earlier for consistency
    print(f"[writer] Started. Will append to {LOG_PATH}. Server port env={port}")

    while True:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{ts}] {rnd}\n"
        with LOG_PATH.open("a", encoding="utf-8") as f:
            f.write(line)
            f.flush()
            os.fsync(f.fileno())
        print(f"[writer] wrote: {line.strip()}")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()

