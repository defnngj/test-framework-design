# loguru_demo2.py
import sys
import time

from loguru import logger

# stderr 配置
logger.remove()

# 自定义log格式
log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</> {file} <level>| {level} | {message}</level>"

# 终端/控制台配置
logger.add(sys.stderr, format=log_format, level="DEBUG")

# log 文件配置
logger.add(f"file_{time.time()}.log", rotation="12:00", format=log_format)

logger.debug("this is a debug!")
logger.info("this is a info!")
logger.warning("this is a warning!")
logger.error("this is a error!")
logger.success("this is a success!")
