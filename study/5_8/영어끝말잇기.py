def solution(n, words):
    answer = []
    for idx,j in enumerate(words):
        if idx > 0:
            if j in answer or words[idx][0] != words[idx-1][-1]:
                return [idx % n + 1, idx // n +1]
            else:
                answer.append(j)
        else:
            answer.append(j)
    return [0,0]