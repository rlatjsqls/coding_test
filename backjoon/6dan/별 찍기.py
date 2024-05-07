import sys

n = int(sys.stdin.readline())

e = n-1
s = 1
while (e>0):
    e = e - 1
    print(' '*e,'*'*s)
    s = s + 2
print('*'*(2*n-1))
while(e<n):
    s = s - 2
    print(' '*e,'*'*s)
    e = e + 1