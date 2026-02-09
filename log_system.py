import logging
import os
from datetime import datetime

LOGS = "logs"

if not os.path.isdir(LOGS):
    os.makedirs(LOGS)

logger = logging.getLogger("2048_Game_System")
logger.setLevel(logging.DEBUG)

log_file = os.path.join(LOGS, f'2048_Game_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
# print(log_file)

file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.DEBUG)

formater = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s -%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

file_handler.setFormatter(formater)
# console_handler.setFormatter(formater)

logger.addHandler(file_handler)
# logger.addHandler(console_handler)


__all__ = [logger]


