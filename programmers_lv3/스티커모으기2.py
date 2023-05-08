def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    arr1 = sticker[:-1]
    arr2 = sticker[1:]
    for i in range(1, len(sticker)-1):
        if i == 1:
            arr1[i] = max(arr1[i],arr1[i-1])
        else:
            arr1[i] = max(arr1[i-1], arr1[i-2]+arr1[i])
    for i in range(1, len(sticker)-1):
        if i == 1:
            arr2[i] = max(arr2[i],arr2[i-1])
        else:
            arr2[i] = max(arr2[i-1], arr2[i-2] + arr2[i])
    return max(arr1[-1], arr2[-1])