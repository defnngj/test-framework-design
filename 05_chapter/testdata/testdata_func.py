import datetime
import random
import re
import time

import requests

# 移动号段
mobile = [134, 135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158, 159, 172,
          178, 182, 183, 184, 187, 188, 195, 197, 198]
# 联通号段
unicom = [130, 131, 132, 145, 155, 156, 166, 175, 176, 185, 186, 196]
# 联通号段
telecom = [133, 149, 153, 180, 181, 189, 173, 177, 190, 191, 193, 199]


def get_phone(operator: str = None) -> str:
    """
    get phone number
    :param operator: 指定运营商
    """
    if operator is None:
        all_operator = mobile + unicom + telecom
        top_third = random.choice(all_operator)
    elif operator == "mobile":
        top_third = random.choice(mobile)
    elif operator == "unicom":
        top_third = random.choice(unicom)
    elif operator == "telecom":
        top_third = random.choice(telecom)
    else:
        raise TypeError("Please select the right operator：'mobile'，'unicom'，'telecom' ")

    suffix = random.randint(9999999, 100000000)

    return f"{top_third}{suffix}"


zh_names_male = list(set(re.split(r"\s+", """德义 苍 鹏云 炎 和志 新霁 澜 星泽 驰轩 楚 宏深 全 波涛 飞文 波 振国 凯 光启 经略 乐天 
志强 作人 英叡 英华 星阑 景龙 鹏鲸 采 浩然 举 芬 鸿才 卫 嘉纳 旭东 玉泽 祺瑞 荫 茂德 博 鸿羲 彦 涵衍 开诚 鸿远 凯歌 星华 玉宇 潍 德华 甲 
梓 正阳 文乐 高杰 骄 腾逸 鸿畅 修平""".strip())))

zh_names_female = list(set(re.split(r"\s+", """海莹 曼珠 虹影 凝安 淳美 清润 旋 馨香 骊霞 水丹 长文 怀薇 平卉 向露 秀敏 青柏 尔阳 奥婷 
智美 雅可 骊燕 燕珺 白曼 春枫 谷之 暖姝 易绿 娅欣 欢 半梅 忆彤 宇 茗 芳洁 双文 艳芳 珍丽 杨 若星 松 葳 晓畅 菱华 新荣 觅露 冰夏 初柳 迎蕾 
海宁 香 妙颜 靖之""".strip())))

zh_last_name = list(set(re.split(r"\s+", """赵 钱 孙 李 周 吴 郑 王 冯 陈 褚 卫 蒋 沈 韩 杨 朱 秦 尤 许 何 吕 施 张 孔 曹 严 华
宇文 尉迟 延陵 羊舌 欧阳 长孙 上官 司徒 司马 夏侯 西门 南宫 公孙""".strip())))


def first_name(gender: str = "") -> str:
    """
    generate first name
    :param gender:
    :return:
    """
    genders = ["", "m", "f", "male", "female"]
    if gender not in genders:
        raise ValueError("Unsupported gender, try [m, f, male, female] instead")

    if gender == "":
        return random.choice(zh_names_female + zh_names_male)
    elif gender == "m":
        return random.choice(zh_names_male)
    else:
        return random.choice(zh_names_female)


def last_name() -> str:
    """
    generate last name
    :return:
    """
    return random.choice(zh_last_name)


def name() -> str:
    """
    generate Chinese name
    """
    return f"{last_name()}{first_name()}"


TAOBAO_TIME = "http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp"


def online_timestamp() -> str:
    """
    get now timestamp
    :return:
    """
    r = requests.get(TAOBAO_TIME)
    data = r.json()
    ts = data["data"]["t"]
    return ts


def online_datetime() -> [str, datetime]:
    """
    get online date time。
    :return:
    """
    ts = online_timestamp()
    date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(ts[:10])))
    return date_time
