num = int(input())

text = []
for i in range(num):
    txt = input()
    text.append(txt)

count = 0
for i in text:
    stack = []
    dict = []
    flag = 0
    for j in i:
        if not stack:
            stack.append(j)
        else:
            if stack[-1] == j:
                continue
            else:
                if j in dict:
                    flag = 1
                    break
                dict.append(stack.pop())
                stack.append(j)
    if flag == 0:
        count += 1
print(count)