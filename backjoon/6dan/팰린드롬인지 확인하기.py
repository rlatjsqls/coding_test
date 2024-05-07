import sys

#text =  sys.stdin.readline()
text = input()
answer = 3
if len(text) == 1:
    answer = 2

elif len(text) % 2 != 0:
    for i in range(0,(len(text)-1)//2):
        if text[i] != text[len(text)-i-1]:
            answer = 1
            break
        answer = 2        

else:
    for i in range(0,(len(text))//2):
        if text[i] != text[len(text)-i-1]:
            answer = 1
            break
        answer = 2

if answer == 2:
    print(1)
else:
    print(0)