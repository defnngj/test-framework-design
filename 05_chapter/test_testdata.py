from testdata.testdata_func import get_phone
from testdata.testdata_func import first_name, last_name, name
from testdata.testdata_func import online_timestamp, online_datetime

# 随机生成手机号
print("手机号:", get_phone())
print("手机号(移动):", get_phone(operator="mobile"))
print("手机号(联通):", get_phone(operator="unicom"))
print("手机号(电信):", get_phone(operator="telecom"))


# 随机生成名字
print("名字：", first_name())
print("名字(男)：", first_name(gender="male"))
print("名字(女)：", first_name(gender="female"))

# 随机一个姓
print("姓:", last_name())

# 随机一个姓名
print("姓名:", name())


# 获取在线时间
print("当前时间戳", online_timestamp())
print("当前日期时间", online_datetime())
