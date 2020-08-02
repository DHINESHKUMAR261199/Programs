n=int(input())
s=''
while n>0:
    s+=str(n%6)
    n//=6
print(int(s[::-1]))
