a,b=int(input()),int(input())
l=[]
for i in range(a-1):
    l.append(0)
l.append(1)
c=a
for i in range(b-a):
    l.append(sum(l[i:c]))
    c+=1
print(*l)
