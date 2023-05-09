def devide_func(x):
    left = 0
    right = 0
    for idx, i in enumerate(x):
        if i == ')':
            right += 1
        else:
            left += 1
        if left == right:
            u = x[:idx+1]
            v = x[idx+1:]
            return u, v
        
def check_func(x):
    stack = []
    for i in x:
        if stack:
            if stack[-1] == '(' and i == ')':
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    if stack:
        return False
    else:
        return True

def func_u(u):
    arr = ""
    for i in u[1:-1]:
        if i == '(':
            arr += ')'
        else:
            arr += '('
    return arr
answer = ""
    
def solution(p):
    global answer
    if len(p) == 0:
        return ''
    u, v = devide_func(p)
    if check_func(u) == True:
        return u + solution(v)
    else:
        arr = ''
        arr += '('
        arr += solution(v)
        arr += ')'
        arr += func_u(u)
        return arr