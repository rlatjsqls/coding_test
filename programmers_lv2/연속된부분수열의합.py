from collections import deque

def solution(sequence, k):
    answer = []
    stack = deque()
    start = 0
    end = -1
    sum_stack = 0
    
    for i in sequence:
        stack.append(i)
        sum_stack += i
        end += 1
        while sum_stack > k:
            sum_stack -= stack.popleft()
            start +=1
        if sum_stack == k:
            answer.append([start, end])
            
    return sorted(answer, key = lambda x : (x[1]-x[0], x[0]))[0]