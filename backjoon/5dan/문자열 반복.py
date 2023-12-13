import sys

T = int(sys.stdin.readline())
for _ in range(T):
    result = ''
    n, s = sys.stdin.readline().split()
    for i in s:
        result += int(n)*i
    print(result)