import logging
import time
from logging import DEBUG


# logging.basicConfig(filename="/Volumes/Entertainme/Automation/goibiboNewProject/Logs/logFile.log", format="%(asctime)s [%(levelname)s] %(name)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S",level=logging.INFO)
# log = logging.getLogger(__name__)
#
# log.info("This is our first log")

# def log():
#     logging.basicConfig(filename="/Volumes/Entertainme/Automation/goibiboNewProject/Logs/logFile.log",
#                         format="%(asctime)s [%(levelname)s] %(name)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)
#     logger = logging.getLogger(__name__)
#     return logger


class Logger():
    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')
        curr_time = time.strftime("%Y-%m-%d")
        self.LogFileName = '/Volumes/Entertainme/Automation/goibiboNewProject/Logs/logFile.log' + curr_time + '.txt'
        fh = logging.FileHandler(self.LogFileName, mode="a")
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)
