from typing import Callable, Text, Tuple
from functools import wraps
import redis
from loguru import logger

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def dependent_func(func_obj: Callable, key_name: Text = None, *out_args, **out_kwargs):
    """
    依赖方法装饰器

    :param func_obj: 方法对象.
    :param key_name: 关键名
    :param out_args:
    :param out_kwargs:
    :return:
    """
    global redis_client
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            depend_func_name = func_obj.__name__

            key = key_name
            if key_name is None:
                key = depend_func_name

            if not redis_client.get(key):
                dependence_res = _call_dependence(func_obj, func_name,*out_args, **out_kwargs)
                redis_client.set(key, dependence_res)

            else:
                logger.info(f"<{depend_func_name}> 已被执行, 通过缓存获取 `{key}`.")
            r = func(*args, **kwargs)
            return r

        return wrapper

    return decorator


def _call_dependence(dependent_api: Callable or Text, func_name: Text, *args, **kwargs):
    """
    执行依赖方法.
    :param dependent_api: 依赖方法
    :param func_name: 方法名
    :param args:
    :param kwargs:
    :return:
    """
    depend_func_name = dependent_api.__name__
    logger.info(f"<{func_name}> 依赖于 <{depend_func_name}>, 执行.")
    res = dependent_api(*args, **kwargs)
    return res
