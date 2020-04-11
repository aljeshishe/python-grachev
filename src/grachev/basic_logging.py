import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pathlib import Path

now = datetime.now().strftime('%y%m%d_%H%M%S')
logs_path = Path('logs')
logs_path.mkdir(parents=True, exist_ok=True)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s|%(levelname)-4.4s|%(thread)s|%(filename)-10.10s|%(funcName)-10.10s|%(message)s',
                    handlers=[logging.StreamHandler(),
                              RotatingFileHandler(logs_path / f'log_{now}.log', maxBytes=200*1024*1024, backupCount=5)
                              ])


logging.info('hello')