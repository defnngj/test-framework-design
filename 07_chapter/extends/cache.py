# extends/cache.py
import os
import json

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(FILE_DIR, "cache_data.json")


class Cache:
    """
    读写JSON文件实现Cache
    """

    def __init__(self):
        """
        初始化cache文件
        """
        is_exist = os.path.isfile(DATA_PATH)
        if is_exist is False:
            with open(DATA_PATH, "w", encoding="utf-8") as json_file:
                json.dump({}, json_file)

    @staticmethod
    def clear(key: str = None) -> None:
        """
        清理cache
        """
        if key is None:
            with open(DATA_PATH, "w", encoding="utf-8") as json_file:
                print("Clear all cache data")
                json.dump({}, json_file)
        else:
            with open(DATA_PATH, "r+", encoding="utf-8") as json_file:
                save_data = json.load(json_file)
                del save_data[key]
                print(f"Clear cache data: {key}")

            with open(DATA_PATH, "w+", encoding="utf-8") as json_file:
                json.dump(save_data, json_file)

    @staticmethod
    def set(data: dict) -> None:
        """
        设置 cache
        """
        with open(DATA_PATH, "r+", encoding="utf-8") as json_file:
            save_data = json.load(json_file)
            for key, value in data.items():
                data = save_data.get(key, None)
                if data is None:
                    print(f"Set cache data: {key} = {value}")
                else:
                    print(f"update cache data: {key} = {value}")
                save_data[key] = value

        with open(DATA_PATH, "w+", encoding="utf-8") as json_file:
            json.dump(save_data, json_file)

    @staticmethod
    def get(name=None):
        """
        查询cache
        """
        with open(DATA_PATH, "r+", encoding="utf-8") as json_file:
            save_data = json.load(json_file)
            if name is None:
                return save_data

            value = save_data.get(name, None)
            if value is not None:
                print(f"Get cache data: {name} = {value}")
            return value


cache = Cache()
