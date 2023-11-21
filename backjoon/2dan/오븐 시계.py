H, m = map(int, input().split())
time = int(input())
x = time // 60
y = time % 60
a = (m + y) // 60
b = (m + y) % 60

print((H+x+a)%24,b)