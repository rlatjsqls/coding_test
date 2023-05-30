def solution(s):
    answer = []
    s = s.lstrip('{').rstrip('}').split('},{')
    dict_s = {}
    for i in s:
        temp = i.split(',')
        for j in temp:
            if j.isdigit():
                if j not in dict_s:
                    dict_s[j] = 1
                else:
                    dict_s[j] += 1
    dict_s = sorted(dict_s.items(), key=lambda x: x[1], reverse=True)
    for i in dict_s:
        answer.append(int(i[0]))
    return answer