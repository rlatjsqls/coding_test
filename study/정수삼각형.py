def solution(triangle):
    answer = 0
    size_tri = len(triangle)
    for i in range(0,len(triangle)):
        for j in range(i,len(triangle)-1):
            triangle[i].append(0)
    for x in range(0,size_tri):
        if x == 0:
            continue
        for y in range(0,size_tri):
            if y == 0:
                triangle[x][0] = triangle[x-1][0] + triangle[x][0]
            else:
                triangle[x][y] = max(triangle[x-1][y] + triangle[x][y],triangle[x-1][y-1] + triangle[x][y])
    return max(triangle[size_tri-1])