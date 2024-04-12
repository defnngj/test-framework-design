import json

import requests
from loguru import logger


def formatting(msg):
    """格式化JSON数据"""
    if isinstance(msg, dict):
        return json.dumps(msg, indent=2, ensure_ascii=False)
    return msg


def request(func):
    """请求装饰器"""

    def wrapper(*args, **kwargs):
        func_name = func.__name__
        logger.info('-------------- 请求 -----------------')
        try:
            url = list(args)[1]
        except IndexError:
            url = kwargs.get("url", "")

        logger.info(f"[method]: {func_name.upper()}      [URL]: {url} ")
        auth = kwargs.get("auth", "")
        headers = kwargs.get("headers", "")
        cookies = kwargs.get("cookies", "")
        params = kwargs.get("params", "")
        data = kwargs.get("data", "")
        json_ = kwargs.get("json", "")
        if auth != "":
            logger.debug(f"[auth]:\n {auth}")
        if headers != "":
            logger.debug(f"[headers]:\n {formatting(headers)}")
        if cookies != "":
            logger.debug(f"[cookies]:\n {formatting(cookies)}")
        if params != "":
            logger.debug(f"[params]:\n {formatting(params)}")
        if data != "":
            logger.debug(f"[data]:\n {formatting(data)}")
        if json_ != "":
            logger.debug(f"[json]:\n {formatting(json_)}")

        # running function
        r = func(*args, **kwargs)

        status_code = r.status_code
        logger.info("-------------- 响应 ----------------")
        if status_code == 200 or status_code == 304:
            logger.info(f"successful with status {status_code}")
        else:
            logger.warning(f"unsuccessful with status {status_code}")
        resp_time = r.elapsed.total_seconds()
        try:
            resp = r.json()
            logger.debug(f"[type]: json      [time]: {resp_time}")
            logger.debug(f"[response]:\n {formatting(resp)}")
        except BaseException as msg:
            logger.debug("[warning]: failed to convert res to json, try to convert to text")
            logger.trace(f"[warning]: {msg}")
            r.encoding = 'utf-8'
            logger.debug(f"[type]: text      [time]: {resp_time}")
            logger.debug(f"[response]:\n {r.text}")

        return r

    return wrapper


class HttpRequest:
    """http request class"""

    @request
    def get(self, url, params=None, **kwargs):
        return requests.get(url, params=params, **kwargs)

    @request
    def post(self, url, data=None, json=None, **kwargs):
        return requests.post(url, data=data, json=json, **kwargs)

    @request
    def put(self, url, data=None, **kwargs):
        return requests.put(url, data=data, **kwargs)

    @request
    def delete(self, url, **kwargs):
        return requests.delete(url, **kwargs)
