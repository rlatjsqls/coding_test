from collections import deque

#bfs로 주어진 노드와 경로에 대해서 연결된 노드의 수를 리턴하여준다.
def func(node, dict_route):
    que = deque([node])
    visited = [node]    #연결된 노드들
    
    #잘렸을때 아무곳도 연결 안되어있는 경우
    if que[0] not in dict_route:
        return 1
    
    while que:
        temp = dict_route[que.popleft()]
        for i in temp:
            if i not in visited:
                visited.append(i)
                que.append(i)
                
    return len(visited)

def solution(n, wires):
    answer = n
    
    for idx in range(len(wires)):
        temp = wires[:]
        #문제에 중복된 연결이 주어지지 않아서 wires의 원소들을 한번씩 끊는 용도로 사용
        x, y = temp.pop(idx)
        #끊어진 상황에서 연결된 상태를 가지고 있는 딕셔너리
        dict_route = {}
        
        for wire in temp:
            if wire[0] in dict_route:
                dict_route[wire[0]].append(wire[1])
            else:
                dict_route[wire[0]] =  [wire[1]]
            if wire[1] in dict_route:
                dict_route[wire[1]].append(wire[0])
            else:
                dict_route[wire[1]] =  [wire[0]]

        if abs(func(x, dict_route) - func(y, dict_route)) < answer:
            answer = abs(func(x, dict_route) - func(y, dict_route))

    return answer