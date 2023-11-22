import sys
T = int(sys.stdin.readline())
values = list(map(int,sys.stdin.readline().split()))
S = int(sys.stdin.readline())
answer = 0

for i in values:
    if i == S:
        answer += 1
print(answer)
