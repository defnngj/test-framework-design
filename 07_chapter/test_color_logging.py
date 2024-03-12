import logging
from extends.color_logging import ColorLog

log = ColorLog(__name__, level=logging.DEBUG, logfile="color_log.log")

log.debug("this is debug")
log.info("this is info")
log.warning("this is warning")
log.error("this is error")
log.critical("this is critical")
