#! /bin/bash
cd /workspace/src/
uvicorn meme_interface:app --reload --host 0.0.0.0 --port 80
