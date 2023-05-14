def solution(rows, columns, queries):
    answer = []
    result = []
    box = [[j*columns + i for i in range(1, columns+1)] for j in range(rows)]
    for i in queries:
        answer = []
        for x in range(i[1]-1,i[3]):
            answer.append(box[i[0]-1][x])
        for x in range(i[0],i[2]):
            answer.append(box[x][i[3]-1])
        for x in range(i[3]-2,i[1]-2,-1):
            answer.append(box[i[2]-1][x])
        for x in range(i[2]-2,i[0]-1,-1):
            answer.append(box[x][i[1]-1])
            
        answer.insert(0, answer.pop())
        result.append(min(answer))
        idx = 0
        for x in range(i[1]-1,i[3]):
            box[i[0]-1][x] = answer[idx]
            idx += 1
        for x in range(i[0],i[2]):
            box[x][i[3]-1] = answer[idx]
            idx +=1
        for x in range(i[3]-2,i[1]-2,-1):
            box[i[2]-1][x] = answer[idx]
            idx +=1
        for x in range(i[2]-2,i[0]-1,-1):
            box[x][i[1]-1] = answer[idx]
            idx += 1
            
    return result
