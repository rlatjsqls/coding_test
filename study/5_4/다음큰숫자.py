def cnt_one(n):
    bi_n = bin(n)[2:]
    cnt_n = 0
    
    for i in bi_n:
        if i == '1':
            cnt_n +=1
    return cnt_n

def solution(n):
    answer = 0
    n_cnt = cnt_one(n)
    n += 1
    
    while 1:
        if n_cnt == cnt_one(n):
            return n
        n += 1