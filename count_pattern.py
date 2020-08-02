from itertools import groupby
def fun(c):
    li=[(i,len(list(j)))for i,j in groupby(str(c))]
    s=''
    for i in li:
        s+=str(i[1])+i[0]
    return s
n=int(input())
if n==1:
    print(1)
else:
    for i in range(n-1):
        if i==0:
            print(1)
            c=1
            c=fun(c)
            print(" ".join(c))
        else:
            c=fun(c)
            print(" ".join(c))
        

