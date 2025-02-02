#!/bin/bash
python3 src/main.py
# Start a simple HTTP server on port 8888
cd public && python3 -m http.server 8888