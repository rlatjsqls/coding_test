H, m = map(int, input().split())

if m < 45:
    if H > 0:
        print(H-1, m + 15)
    else:
        print(23, m + 15)
else:
    print(H, m-45)