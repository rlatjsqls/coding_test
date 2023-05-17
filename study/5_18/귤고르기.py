def solution(k, tangerine):
    answer = 0
    dic_t = {}
    for i in tangerine:
        if i in dic_t.keys():
            dic_t[i] = dic_t[i] + 1
        else:
            dic_t[i] = 1
    arr = sorted(dic_t.items(), key=lambda x: x[1], reverse=True)
    for i in arr:
        k -= i[1]
        answer += 1
        if k <= 0:
            return answer