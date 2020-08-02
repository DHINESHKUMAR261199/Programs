n=int(input())
a,b=3,2
l=[]
for i in range((n*(n+1))//2):
    s=("0"*4+str(a*b))[-5::]
    l.append(s)
    a,b=a+4,b+2   
x,y=0,1
for i in range(n):
    for k in range(n-1-i):
        print(end=" "*5)
    for j in l[x:y]:
        print(j,end=" "*5)
    for k in range(n-1-i):
        print(end=" "*5)
    x,y=y,y+2+i
    print()
