def solution(cacheSize, cities):
    cache = []
    answer = 0
    new_cities = []
    for i in cities:
        new_cities.append(i.lower())
        
    if cacheSize == 0:
        return len(cities)*5
    
    for i in new_cities:
        if i in cache:
            answer += 1
            cache.remove(i)
        else:
            answer += 5
        if len(cache) == cacheSize:
                cache.pop(0)
        cache.append(i)
    return answer