import sys

while(1):
    x = sys.stdin.readline().rstrip()
    if x == '':
        break
    a, b = map(int, x.split())
    print(a+b)