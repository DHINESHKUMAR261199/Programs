from itertools import combinations
from math import gcd
te=int(input())
ans=[]
for i in range(te):
    n=int(input())
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    print(l)
    a=list(combinations(l,2))
    print(a)
    c=0
    for i in range(len(a)):
        if gcd(a[i][0],a[i][1])==1:
            c+=1
    ans.append(c)
for i in ans:
    print(i)
