def func(n):
    result = 1
    while n != 1:
        result *= n - 1
        n-=1
    return result

def solution(n, k):
    answer = []
    k -= 1
    test = [i for i in range(1,n+1)]
    x = func(n)
    for i in range(n-1,1,-1):
        answer.append(test.pop(k // x))
        k = k % x
        x //= i
    if k == 0:
        answer.append(test.pop(0))
        answer.append(test.pop(0))
    else:
        answer.append(test.pop(1))
        answer.append(test.pop(0))
    return answer