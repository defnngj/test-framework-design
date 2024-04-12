import json
import time

from jmespath import search
from loguru import logger


def check_response(
        describe: str = "",
        status_code: int = 200,
        ret: str = None,
        check: dict = None,
        debug: bool = False):
    """
    检查返回的 response 数据
    :param describe: 接口描述
    :param status_code: 断言状态码
    :param ret: 提取返回的数据
    :param check: 检查接口返回的数据
    :param debug: 日志开关 Ture/False
    :return:
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            if debug is True:
                logger.info(f"Execute {func_name} - args: {args}")
                logger.info(f"Execute {func_name} - kwargs: {kwargs}")

            r = func(*args, **kwargs)
            flat = True
            if r.status_code != status_code:
                logger.info(f"Execute {func_name} - {describe} failed: {r.status_code}")
                flat = False

            try:
                r.json()
            except json.decoder.JSONDecodeError:
                logger.info(f"Execute {func_name} - {describe} failed：Not in JSON format")
                flat = False

            if debug is True:
                logger.info(f"Execute {func_name} - response:\n {r.json()}")

            if flat is True:
                logger.info(f"Execute {func_name} - {describe} success!")

            if check is not None:
                for expr, value in check.items():
                    data = search(expr, r.json())
                    if data != value:
                        logger.error(f"Execute {func_name} - check data failed：{value}")
                        raise ValueError(f"{data} != {value}")

            if ret is not None:
                data = search(ret, r.json())
                if data is None:
                    logger.warning(f"Execute {func_name} - return {ret} is None")
                return data
            else:
                return r.json()

        return wrapper

    return decorator


def timer(func):
    """
    计时器装饰器
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"{func.__name__} executed in {end_time - start_time:.3f}s")
        return result

    return wrapper
