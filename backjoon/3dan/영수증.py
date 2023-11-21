total = int(input())
T = int(input())
result = 0
for i in range(T):
    P, C = map(int, input().split())
    result += P*C

if result == total:
    print('Yes')
else:
    print('No')