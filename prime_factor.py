def p(n):
    l=[]
    while n%2==0:
        l.append(2)
        n/=2
    for i in range(3,int((n**0.5)+1),2):
        while n%i==0:
            l.append(int(i))
            n/=i
    if n>2:
        l.append(int(n))
    return l
def s(n):
    c=0
    for i in str(n):
        c+=int(i)
    return c
n=int(input())
for i in range(4,n+1):
    b=s(i)
    c=0
    a=p(i)
    if len(a)>1:
        for j in a:
            c+=s(j)
    if c==b:
        print(i,end=" ")
