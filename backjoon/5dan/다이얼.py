import sys

s = sys.stdin.readline().rstrip()
dict = {'ABC' : 3, 'DEF' : 4, 'GHI' : 5, 'JKL' : 6, 'MNO': 7, 'PQRS':8,'TUV':9, "WXYZ":10}
result = 0
for j in s:
    for i in dict:
        if j in i:
            result += dict[i]

print(result)