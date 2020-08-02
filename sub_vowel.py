s=input()
n=int(input())
l=len(s)
t=[]
for i in range(l):
    for j in range(i+1,l+1):
        t.append(s[i:j])
v=['a','e','i','o','u','A','E','I','O','U']
a=[]
for i in t:
    x=""
    for j in i:
        if j in v:
            x+=j
    if len(set(x))==n:
        a.append(i)
print(len(max(a,key=len)))
    
