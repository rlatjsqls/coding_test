from collections import deque

def solution(queue1, queue2):
    answer = 0
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    size = len(queue1) * 4
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    while (sum_queue1 != sum_queue2):
        if sum_queue1 > sum_queue2:
            temp = queue1.popleft()
            queue2.append(temp)
            sum_queue1 -= temp
            sum_queue2 += temp
            answer += 1
        elif sum_queue2 > sum_queue1:
            temp = queue2.popleft()
            queue1.append(temp)
            sum_queue2 -= temp
            sum_queue1 += temp
            answer += 1
        if len(queue1) == 0 or len(queue2) == 0 or answer > size:
            return -1
    return answer