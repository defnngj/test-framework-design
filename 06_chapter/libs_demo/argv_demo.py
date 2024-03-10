# argv_demo.py
import sys


run_file = sys.argv[0]
print(f"file name -> {run_file}")

args = sys.argv[1:]
for i in args:
    print(f"hello, {i}")
