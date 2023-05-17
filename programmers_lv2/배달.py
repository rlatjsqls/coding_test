from collections import deque

def bfs(dict_road, k):
    visited = {1:0}
    que = deque([1])
    cnt = 0
    while que:
        a = que.popleft()
        for i in dict_road[a]:
            if i[0] not in visited:
                visited[i[0]] = visited[a]+i[1]
                que.append(i[0])
            elif i[0] in visited and visited[i[0]] > visited[a]+i[1]:
                visited[i[0]] = visited[a]+i[1]
                que.append(i[0])
    for i in visited.values():
        if i <= k:
            cnt += 1
    return cnt
            
            
def solution(N, road, K):
    dict_road = {}
    
    for i in road:
        if i[0] not in dict_road:
            dict_road[i[0]] = [[i[1],i[2]]]
        else:
            dict_road[i[0]].append([i[1],i[2]])
        if i[1] not in dict_road:
            dict_road[i[1]] = [[i[0],i[2]]]
        else:
            dict_road[i[1]].append([i[0],i[2]])
    bfs(dict_road, K)
    
    return bfs(dict_road, K)