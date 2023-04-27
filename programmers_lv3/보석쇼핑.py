from collections import Counter

def solution(gems):
    size = len(set(gems))
    answer = []
    
    left = 0
    gems_dict = Counter()
    for right in range(len(gems)):
        gems_dict[gems[right]] += 1
        right += 1
        while len(gems_dict) == size:
            gems_dict[gems[left]] -=1
            if gems_dict[gems[left]] == 0:
                del gems_dict[gems[left]]
            left +=1
            answer.append([left,right])
            
    return sorted(answer, key = lambda x : (x[1]-x[0], x[0]))[0]