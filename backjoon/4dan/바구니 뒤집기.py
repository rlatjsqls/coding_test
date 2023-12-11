import sys

M, N = map(int, sys.stdin.readline().split())
list = [i+1 for i in range(M)]

for i in range(N):
    x,y = map(int, sys.stdin.readline().split())
    if y-x == 1:
        list[x-1], list[y-1] = list[y-1], list[x-1]
    else:
        for j in range((y-x)//2+1):
            list[x-1+j], list[y-1-j] = list[y-1-j], list[x-1+j]
        
print(' '.join(str(x) for x in list))