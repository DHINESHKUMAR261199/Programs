n=int(input())
l=[]
l.append(1)
l.append(2)
for i in range(1,n):
    a=l[i]
    if i==1:
        l.append(i+1)
    else:
        for j in range(a):
            l.append(i+1)
print(*l[:n])
