#!/usr/bin/env python3
import os
import signal
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

APP_NAME = "todo-app"

class TodoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # simple health root; expand to real todo features later
        if self.path in ("/", "/healthz", "/ready"):
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(f"{APP_NAME} OK\n".encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    # Silence default logging to keep container logs clean
    def log_message(self, fmt, *args):
        return

def main():
    port = int(os.environ.get("PORT", "8080"))

    # Print the required startup message
    print(f"Server started in port {port}", flush=True)

    server = HTTPServer(("0.0.0.0", port), TodoHandler)

    # Graceful shutdown on SIGTERM (Kubernetes)
    def handle_sigterm(signum, frame):
        try:
            server.shutdown()
        finally:
            sys.exit(0)

    signal.signal(signal.SIGTERM, handle_sigterm)
    signal.signal(signal.SIGINT, handle_sigterm)

    server.serve_forever()

if __name__ == "__main__":
    main()

