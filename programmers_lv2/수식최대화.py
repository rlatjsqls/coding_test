def func(op, num, x):
    idx = 0
    while idx != len(op):
        if op[idx] == x:
            if x == '*':
                cal = int(num.pop(idx)) * int(num.pop(idx))
            elif x == '+':
                cal = int(num.pop(idx)) + int(num.pop(idx))
            elif x == '-':
                cal = int(num.pop(idx)) - int(num.pop(idx))
            num.insert(idx,cal)
            op.pop(idx)
            if len(op) == 0:
                break
            idx = 0
            continue
        idx +=1
    return op, num
            

def solution(expression):
    answer = 0
    result = []
    op_order = [['*','+','-'],['*','-','+'],["+",'*','-'],['+','-','*'],['-','*','+'],['-','+','*']]
    op = []
    num = []
    temp = ''
    
    #expression 숫자와 연산자로 나눔
    for i in expression:
        if i.isdigit() == True:
            temp += i
        else:
            num.append(temp)
            temp = ''
            op.append(i)
    num.append(temp)
    
    real_op = op[:]
    real_num = num[:]

    for i in op_order:
        op = real_op[:]
        num = real_num[:]
        for j in i:
            op, num = func(op, num, j)
        if answer < abs(num[0]):
            answer = abs(num[0])
    return answer