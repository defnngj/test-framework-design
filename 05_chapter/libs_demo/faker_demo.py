# faker_demo.py
from faker import Faker

fake = Faker(locale='zh_CN')

# 基本常用数据
name = fake.name()
address = fake.address()
phone = fake.phone_number()
ID = fake.ssn(min_age=18)

print(f"""
    name: {name},
    address: {address}, 
    phone: {phone}, 
    ID: {ID}""")

# 日期时间相关
day_of_month = fake.day_of_month()
day_of_week = fake.day_of_week()
date = fake.date(pattern="%Y-%m-%d")
date_between = fake.date_between(start_date="-30y", end_date="today")
future_datetime = fake.future_datetime(end_date="+30d",)
past_datetime = fake.past_datetime(start_date="-30d", )

print(f"""
    day_of_month: {day_of_month},
    day_of_week: {day_of_week},
    data: {date},
    date_between: {date_between},
    future_datetime: {future_datetime},
    past_datetime: {past_datetime}""")

# 网络相关
email = fake.ascii_free_email()
domain = fake.domain_name(levels=1)
host = fake.hostname()
image_url = fake.image_url()
url = fake.url()
uri = fake.uri()
ipv4 = fake.ipv4(network=False)
ipv6 = fake.ipv6(network=False)

print(f"""
    email: {email},
    domain: {domain},
    host: {host},
    image_url: {image_url},
    url: {url},
    uri: {uri},
    ipv4: {ipv4},
    ipv6: {ipv6}""")
