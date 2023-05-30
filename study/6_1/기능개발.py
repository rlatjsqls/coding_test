def solution(progresses, speeds):
    answer = []
    while progresses:
        for idx, (i, j) in enumerate(zip(progresses, speeds)):
            progresses[idx] = i + j
        if progresses[0] >= 100:
            count = 0
            while progresses and progresses[0]>=100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            if count > 0:
                answer.append(count)
    return answer