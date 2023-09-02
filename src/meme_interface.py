"""JINS MEMEのWebSocketを受けるインターフェース
"""
import sys
import time
from logging import getLogger, Logger, Handler, StreamHandler, DEBUG
default_logger: Logger = getLogger(__name__)
handler: Handler = StreamHandler()
handler.setLevel(DEBUG)
default_logger.addHandler(handler)
default_logger.setLevel(DEBUG)
default_logger.propagate = False

from fastapi import FastAPI, WebSocket
from sample import Sample

app = FastAPI()
sample = Sample(logger=default_logger)

@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        sample.print(data, "accX")
