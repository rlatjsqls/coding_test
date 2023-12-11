import sys

M, N = map(int,sys.stdin.readline().split())

result = [i for i in range(1,M+1)]
for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    result[x-1], result[y-1] = result[y-1],result[x-1]

print(' '.join(str(z) for z in result))