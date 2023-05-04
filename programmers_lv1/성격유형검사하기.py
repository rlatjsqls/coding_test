def solution(survey, choices):
    answer = ''
    answer_dict = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    
    for alp, choice in zip(survey,choices):
        if choice-4 < 0:
            answer_dict[alp[0]] += abs(choice-4)
        elif choice-4 > 0:
            answer_dict[alp[1]] += choice-4
    if answer_dict['R'] < answer_dict['T']:
        answer += 'T'
    else:
        answer += 'R'
    if answer_dict['C'] < answer_dict['F']:
        answer += 'F'
    else:
        answer += 'C'
    if answer_dict['J'] < answer_dict['M']:
        answer += 'M'
    else:
        answer += 'J'
    if answer_dict['A'] < answer_dict['N']:
        answer += 'N'
    else:
        answer += 'A'
        
    return answer