def p(n):
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 0
        else:
            return 1
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))
l,r=map(int,input().split())
c=0
for i in a[l:r+1]:
    if p(i):
        c+=1
print(c)
