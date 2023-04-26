def solution(s):
    answer = ""
    arr = s.split(" ")
    arr_max = int(arr[0])
    arr_min = int(arr[0])
    for i in arr:
        if int(i) > arr_max:
            arr_max = int(i)
        if int(i) < arr_min:
            arr_min = int(i)
    answer = str(arr_min) + " " + str(arr_max)
    return answer