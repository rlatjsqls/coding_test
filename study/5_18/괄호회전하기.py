def count_x(arr):
    stack = []
    for i in arr:
        if stack:
            if stack[-1] == '[' and i == ']' or stack[-1] == '(' and i == ')' or stack[-1] == '{' and i == '}':
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    if stack:
        return 1
    else:
        return 0

def solution(s):
    answer = 0
    arr = list(s)
    for i in range(len(arr)):
        arr.append(arr.pop(0))
        if count_x(arr) == 0:
            answer += 1
    return answer