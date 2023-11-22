import sys
arr = []
for i in range(9):
    x = int(sys.stdin.readline())
    arr.append(x)

print(max(arr))
print(arr.index(max(arr))+1)