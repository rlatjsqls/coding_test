import sys

result = []

for i in range(10):
    n = int(sys.stdin.readline())
    if (n % 42) not in result:
        result.append(n%42)

print(len(result))