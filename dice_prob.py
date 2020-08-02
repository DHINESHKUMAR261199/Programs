import itertools
t=int(input())
for i in range(t):
    c=0
    n,m=map(int,input().split())
    a=list(itertools.product(range(1,m+1), repeat=n))
    print(a)
    for i in a:
        if len(set(i))==n:
            c+=1
    print(c)
    print("{:.4f}".format(c/len(a)))
        




