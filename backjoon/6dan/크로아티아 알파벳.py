text = input()

answer = len(text)
count = 0
for i in range(0,len(text)):
    if text[i] == '=':
        if i-2>=0 and text[i-1] == 'z' and text[i-2] =='d':
            count += 2
        else:
            count += 1

    elif text[i] == '-':
        count += 1

    elif text[i] == 'j':
        if i-1>=0 and text[i-1] == 'l':
            count +=1
        elif i-1>=0 and text[i-1] == 'n':
            count  +=1

print(answer - count)