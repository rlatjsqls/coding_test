import sys

dict = {'A+' : 4.5, 'A0':4.0, 'B+':3.5,
        'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0, 'F':0.0}

grade = 0.0
count = 0.0
for i in range(20):
    a = sys.stdin.readline().split()
    if a[-1] not in dict:
        continue
    grade += float(a[-2]) * dict[a[-1]]
    count += float(a[-2])

result = grade / count
print(result)