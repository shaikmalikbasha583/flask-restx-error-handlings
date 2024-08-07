import os
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime


logging.getLogger(__name__)
logging.root.setLevel(logging.INFO)

fmt_str = r"[%(asctime)s] - %(name)s - P%(process)s - %(levelname)s: %(message)s"

formatter = logging.Formatter(fmt=fmt_str, datefmt="%Y-%m-%d %H:%M:%S")

stream_handler = logging.StreamHandler()

file_handler = TimedRotatingFileHandler(
    os.path.join(os.getcwd(), "logs", "app-logs.log"),
    interval=1,
    when="midnight",
    backupCount=7,
)
file_handler.setLevel(logging.INFO)
stream_handler.setLevel(logging.INFO)

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logging.root.addHandler(file_handler)
logging.root.addHandler(stream_handler)

logging.info("Info")
logging.warning("Warning")
logging.error("Error")
