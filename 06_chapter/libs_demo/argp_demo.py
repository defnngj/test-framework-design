# argp_demo.py
import argparse

parser = argparse.ArgumentParser(description='argparse 简单用法')

parser.add_argument('-n', '--name', type=str, default="tom", help="请输入name名字，默认 tom")
parser.add_argument('-c', '--count', type=int, default=1, help="请输入次数，默认1")

args = parser.parse_args()

# 使用参数
name = args.name
count = args.count
for _ in range(count):
    print(f"hello, {name}")
