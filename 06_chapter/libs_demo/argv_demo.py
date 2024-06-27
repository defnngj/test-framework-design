# argv_demo.py
import sys

run_file = sys.argv[0]
print(f"file name -> {run_file}")

params = sys.argv[1:]
for i in params:
    print(f"hello, {i}")
