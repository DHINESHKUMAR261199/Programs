n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(n):
    for j in range(i+1,n+1):
        print(l[i:j])
        x=sorted(l[i:j])
        if len(x)>1:
            l1.append(x[-2::])
c=0
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
        c+=1
print(c)
