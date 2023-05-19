def solution(jobs):
    size = len(jobs)
    answer, time = 0, 0
    jobs.sort()
    wait, work = [], []
    
    while jobs or work or wait:
        while jobs and jobs[0][0] == time:
            wait.append(jobs.pop(0))

        if work:
            if work[0][1] == time:
                w = work.pop()
                answer += time - w[0]
        if not work:
            if wait:
                wait.sort(key=lambda x: -x[1])
                w2 = wait.pop()
                work.append([w2[0], time+w2[1]])
        time += 1
    return answer // size