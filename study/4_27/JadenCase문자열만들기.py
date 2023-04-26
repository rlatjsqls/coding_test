def solution(s):
    answer = ''
    for i in s.split(' '):
        if answer == '': # 첫글자인경우
            answer += i.capitalize()
        else:            # 그이후 글자
            answer += ' '+i.capitalize()
    return answer