def solution(s):
    answer = 0
    cycle = 0
    while s != '1':
        cnt = 0
        for i in s:
            if i != '1':
                cnt += 1
        answer += cnt
        cycle += 1
        s = bin(len(s) - cnt)[2:]
    return [cycle, answer]