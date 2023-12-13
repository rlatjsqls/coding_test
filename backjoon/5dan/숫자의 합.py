import sys

T = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
result = 0

for i in range(T):
    result += int(s[i])

print(result)