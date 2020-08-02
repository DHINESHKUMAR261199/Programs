def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i == 0:
                return 0
                break
        else:
            return 1
    else:
        return 0
l,r=map(int,input().split())
c=0
for i in range(l,r+1):
    if prime(bin(i)[2::].count("1")):
        c+=1
print(c)
