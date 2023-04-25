def solution(N, number):
    arr = {1:{N}}
    if number == N:
        return 1
    for i in range(2,9):
        test = {int(str(N)*i)}
        for j in range(1,i):
            for x in arr[j]:
                for y in arr[i-j]:
                    test.add(x+y)
                    test.add(x-y)
                    test.add(x*y)
                    if y != 0:
                        test.add(x//y)
        if number in test:
            return i
        
        arr[i] = test
    return -1