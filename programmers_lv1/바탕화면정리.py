def solution(wallpaper):
    answer = []
    min_lux = 50
    min_luy = 50
    max_lux = 0
    max_luy = 0
    
    for luy, i in enumerate(wallpaper):
        for lux, j in enumerate(i):
            if j == '#':
                answer.append([lux,luy])

    
    for x in answer:
        if min_lux > x[0]:
            min_lux = x[0]
        if max_lux < x[0]:
            max_lux = x[0]
        if min_luy > x[1]:
            min_luy = x[1]
        if max_luy < x[1]:
            max_luy = x[1]
    
    return [min_luy,min_lux,max_luy+1,max_lux+1]