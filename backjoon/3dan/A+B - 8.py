import sys
T = int(sys.stdin.readline().rstrip())
for i in range(1, T+1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print('Case #{}: {} + {} = {}'.format(i, a, b, a+b))