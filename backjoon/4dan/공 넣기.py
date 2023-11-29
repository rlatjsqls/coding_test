import sys

N, M = map(int, sys.stdin.readline().split())
result = [0 for i in range(N)]

for i in range(M):
    a,b,c = map(int, sys.stdin.readline().split())
    for j in range(a-1,b):
        result[j] = c

print(' '.join(map(str,result)))