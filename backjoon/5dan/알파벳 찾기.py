import sys

s = sys.stdin.readline().rstrip()
box = ['-1' for i in range(26)]

for num,i in enumerate(s):
    if box[ord(i)-97] == '-1':
        box[ord(i)-97] = str(num)

print(' '.join(box))