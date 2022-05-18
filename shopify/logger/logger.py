import logging
import os
import datetime
from pathlib import Path
from shopify.util.configUtil import ConfigUtil
from shopify.util.singletonType import SingletonType

class MyLogger(metaclass=SingletonType):

    def __init__(self):

        self._configUtil = ConfigUtil()
        self._logger = logging.getLogger()
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s \t [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s')

        now = datetime.datetime.now()
        dirPath = Path(self._configUtil.getLogDirPath())

        if not os.path.isdir(dirPath):
            os.mkdir(dirPath)

        logFileAbsolutePath = os.path.join(dirPath, "log_" + now.strftime("%Y-%m-%d")+".log")
        fileHandler = logging.FileHandler(logFileAbsolutePath)

        streamHandler = logging.StreamHandler()

        fileHandler.setFormatter(formatter)
        streamHandler.setFormatter(formatter)

        self._logger.addHandler(fileHandler)
        self._logger.addHandler(streamHandler)

        print("[LOGGER] Generating new logger instance")
        print("[LOGGER] Log files set to dump at : {}".format(logFileAbsolutePath))

    def get_logger(self):
        return self._logger

logger = MyLogger.__call__().get_logger()

if __name__ == "__main__":
    pass