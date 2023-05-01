def solution(keymap, targets):
    answer = []
    for target in targets:
        answer_temp = []
        for alpha in target:
            temp = []
            for key in keymap:
                key_list = list(key)
                if alpha in key_list:
                    temp.append(key_list.index(alpha)+1)
            if temp:
                answer_temp.append(min(temp))
            #모든 keymap에 target값이 없는 경우
            else:
                answer_temp = [-1]
                break
        answer.append(sum(answer_temp))
    return answer