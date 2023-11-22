import sys
T, Q = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
result = []

for i in arr:
    if i < Q:
        result.append(i)

print(' '.join(map(str,(result))))