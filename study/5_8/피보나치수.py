def fib(n):
    x, y = 0, 1
    for _ in range(n):
        x, y = y, x + y
    return x

def solution(n):
    
    return fib(n) % 1234567