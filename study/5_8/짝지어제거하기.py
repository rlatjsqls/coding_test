def solution(arr):
    stack = []
    for i in arr:
        if stack:
            curr = stack[-1]
            if curr == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    if stack:
        return 0
    else:
        return 1