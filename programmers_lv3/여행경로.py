def func(dict_route):
    stack = ['ICN']
    temp = []
    t = 1
    while t != 0:
        x = stack[-1]
        if dict_route[x]:
            stack.append(dict_route[x].pop(0))
        else:
            a = stack.pop()
            temp.append(a)
        t = 0
        for i in dict_route.values():
            t += len(i)
    stack.extend(temp[::-1])
    return stack
        
def solution(tickets):
    answer = []
    dict_route = {}
    for ticket in tickets:
        if ticket[0] not in dict_route:
            dict_route[ticket[0]] = [ticket[1]]
        else:
            dict_route[ticket[0]].append(ticket[1])
        if ticket[1] not in dict_route:
            dict_route[ticket[1]] = []
    
    for key, item in dict_route.items():
        dict_route[key] = sorted(item)
    return func(dict_route)