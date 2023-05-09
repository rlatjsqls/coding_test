def solution(brown, yellow):
    size = brown + yellow
    for width in range(1, size+1, 1):
        if size % width == 0:
            vertical = size / width
            if width >= vertical and (width-2) * (vertical-2) == yellow:
                return[width,vertical]