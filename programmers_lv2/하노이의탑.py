answer = []
def h(n, start, end, aux):
    if n == 1:
        answer.append([start, end])       
        return
    
    h(n-1, start, aux, end)
    answer.append([start, end])
    h(n-1, aux, end, start)
    

def solution(n):
    global answer
    h(n,1,3,2)
    return answer