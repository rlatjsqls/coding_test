from itertools import combinations

def solution(orders, course):
    avail_list = []
    orders_dict = {}
    
    #orders를 가지고 course의 갯수로 만들수 있는 조합을 만들어서 딕셔너리로 조합의 갯수를 확인
    for number in course:
        for order in orders:
            if len(order) >= number:
                comb_list = list(combinations(order,number))
                for arg in comb_list:
                    result = ''.join(sorted(arg))
                    if result in orders_dict:
                        orders_dict[result] += 1
                    else:
                        orders_dict[result] = 1
    
    #주문중 2번이상 주문된것만 세트로 만들어지기 때문에 value가 2이상인 것들만 따로 리스트에 넣어주었다.
    for i in orders_dict:
        if orders_dict[i] >= 2:
            avail_list.append([i,orders_dict[i]])
    
    #각 course중에서 가장 주문이 많이된것만 세트로 만들어지기 때문에 각각의 course와 길이가 맞는 세트중에 가장 많이 팔린것만 넣어줌
    course_list = []
    for i in course:
        temp = []
        max_val = 0
        for j in avail_list:
            if i == len(j[0]):
                if max_val < j[1]:
                    max_val = j[1]
                    temp = [j[0]]
                elif max_val == j[1]:
                    temp.append(j[0])
        if temp:
            course_list.append(temp)
    
    # 하나의 리스트로 합치기
    result = []
    for i in course_list:
        result.extend(i)
        
    return sorted(result)