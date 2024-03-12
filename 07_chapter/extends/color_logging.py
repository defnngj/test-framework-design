# color_logging.py
import logging
from logging import FileHandler
from logging import StreamHandler

from colorama import Fore, Style


class MyLog:

    def __init__(self, name=__name__, level=logging.DEBUG, logfile="log.log"):
        """
        日志基本配置
        :param name: 模块名字
        :param level: 日志级别
        :param logfile: 日志文件
        """
        # 自定义日志格式
        formatter = logging.Formatter('[%(asctime)s] %(name)s - %(levelname)s - %(message)s')

        # 自定义日志格式
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # 标准流处理
        stream_handler = StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

        # 文件处理器
        file_handler = FileHandler(filename=logfile)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def debug(self, message: str) -> None:
        """ debug log """
        self.logger.debug(Fore.CYAN + str(message) + Style.RESET_ALL)

    def info(self, message: str) -> None:
        """ info log """
        self.logger.info(Fore.GREEN + str(message) + Style.RESET_ALL)

    def warning(self, message: str) -> None:
        """ warning log """
        self.logger.warning(Fore.YELLOW + str(message) + Style.RESET_ALL)

    def error(self, message: str) -> None:
        """ error log """
        self.logger.error(Fore.RED + str(message) + Style.RESET_ALL)

    def critical(self, message: str) -> None:
        """ critical log """
        self.logger.critical(Fore.BLUE + str(message) + Style.RESET_ALL)


if __name__ == '__main__':
    log = MyLog()
    log.logger.debug("this is debug")
