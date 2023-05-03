from collections import deque

def solution(order):
    answer = 0
    size = len(order) + 1
    stack = []
    order = deque(order)
    for i in range(1, size):
        stack.append(i)
        while stack and stack[-1] == order[0]:
            stack.pop()
            order.popleft()
            answer+=1
    return answer