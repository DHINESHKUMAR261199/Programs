n=int(input())
def f(n):
    l=[]
    for i in range(n-1,0,-1):
        if n%i==0:
            l.append(i)
    return l
print(n,end=" ")
while n!=0:
    s=f(n)
    print(sum(s),end=" ")
    n=sum(s)
    
