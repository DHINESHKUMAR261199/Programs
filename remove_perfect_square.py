from itertools import combinations as c
n=input()
l=len(n)
d=[]
for i in range(1,l+1):
    for j in list(c(n,i)):
        t=[]
        s=int("".join(j))
        t.append(s)
        t.append(len(str(s)))
        d.append(t)
d=sorted(d,key=lambda x:(-x[1],x[0]))
f=1
for i in d:
    a=i[0]
    if a!=0 and int((a**0.5))**2==a:
        print(a)
        f=0
        break
if f:
    print(-1)
