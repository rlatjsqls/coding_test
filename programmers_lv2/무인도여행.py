from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x, y, r, c, visited, maps):
    q = deque([(x, y)])
    visited[x][y] = 1
    cost = int(maps[x][y])

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] != 'X':
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    cost += int(maps[nx][ny])
                    q.append((nx, ny))

    return visited, cost   
    
def solution(maps):
    answer = []
    r, c = len(maps), len(maps[0])
    visited = [[0]*c for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                visited, ans = bfs(i, j, r, c, visited, maps)
                answer.append(ans)
    
    if answer:
        return sorted(answer)
    else:
        return [-1]