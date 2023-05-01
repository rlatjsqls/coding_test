def solution(ingredient):   #빵1 - 야채2 - 고기3 - 빵1
    answer = 0
    stack = []
    for item in ingredient:
        if stack:
            if len(stack) > 2 and item == 1:
                if stack[-1] == 3 and stack[-2] ==2 and stack[-3] == 1:
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    answer += 1
                else:
                    stack.append(item)
            else:
                stack.append(item)
        else:
            stack.append(item)
    return answer