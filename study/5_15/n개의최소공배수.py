def cal_g(x,y):
    for i in range(1,x*y+1):
        if i % x == 0 and i % y == 0:
            return i
    return x*y

def solution(arr):
    a = arr[0]
    for i in range(0,len(arr)-1):
        a = cal_g(a,arr[i+1])
    return a