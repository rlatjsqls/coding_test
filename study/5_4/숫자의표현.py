def solution(n):
    answer = 0
    for i in range(1, n+1, 1):
        sum_i = 0
        while sum_i < n:
            sum_i += i
            i += 1
        if sum_i == n:
            answer += 1
    return answer