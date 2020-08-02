s=input()
n=len(s)
l=[]
for i in range(n):
    for j in range(i+1,n+1):
        l.append(s[i:j])
t=[]
for i in range(len(l)):
    if l[i] in l[i+1:]:
        t.append(l[i])
print(max(t,key=len))
