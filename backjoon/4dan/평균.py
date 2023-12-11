import sys

N = int(sys.stdin.readline())
list = list(map(int,sys.stdin.readline().split()))

Z = max(list)
for i in range(N):
    list[i] = (list[i] / Z) * 100

print(sum(list)/N)