import sys

result = [0 for i in range(30)]

for i in range(28):
    x = int(sys.stdin.readline())
    result[x-1] = 1

for i in range(30):
    if result[i] == 0:
        print(i+1)