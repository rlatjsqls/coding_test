import sys

a, b = map(int, sys.stdin.readline().split())
if int(str(a)[::-1]) > int(str(b)[::-1]):
    print(str(a)[::-1])
else:
    print(str(b)[::-1])