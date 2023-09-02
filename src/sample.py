"""JINS MEMEのWebSocketを受けて動くサンプル
"""
import json

from logging import getLogger, Logger, Handler, NullHandler
null_logger: Logger = getLogger(__name__)
handler: Handler = NullHandler()
null_logger.addHandler(handler)
null_logger.propagate = False

class Sample:
    def __init__(self, logger: Logger | None = None):
        self.logger: Logger = logger or null_logger

    def print_all(self, data_txt: str):
        data = json.loads(data_txt)
        self.logger.info(data)

    def print(self, data_txt: str, key: str):
        data = json.loads(data_txt)
        self.logger.info(data[key])
