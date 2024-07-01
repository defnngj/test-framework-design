# test_sys_logging.py
import logging

from extends.my_logging import MyLog

log = MyLog(__name__, level=logging.DEBUG, logfile="./log/my_log.log")

log.debug("this is debug")
log.info("this is info")
log.warning("this is warning")
log.error("this is error")
log.critical("this is critical")
