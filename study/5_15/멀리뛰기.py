def fibo(n):
    a, b = 1, 1
    for _ in range(n):
        a, b  = b, a+b
    return a

def solution(n):
    
    return fibo(n) % 1234567
