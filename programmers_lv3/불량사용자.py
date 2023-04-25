from itertools import permutations

# 입력된 아이디와 입력된 벤될 아이디가 맞으면 1 아니면 -1
def check_id(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return -1
    for i,j in zip(user_id, banned_id):
        if j.isalpha() == True and i != j:
            return -1
    return 1

def solution(user_ids, banned_ids):
    answer = []
    size = len(banned_ids)
    permu_result = list(permutations(user_ids,size))
    
    for x in permu_result:
        flag = 3
        for y, z in zip(x, banned_ids):
            if check_id(y, z) == -1:
                flag = 1
        if flag == 3:
            b = set(x)
            if b not in answer:
                answer.append(b)
    return len(answer)