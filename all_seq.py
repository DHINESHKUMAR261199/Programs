#SubSequences ... (2^n)-1
from itertools import combinations as c
n=input()
l=len(n)
for i in range(1,l+1):
    for j in list(c(n,i)):
        print("".join(j))
print("*"*20)
#SubArrays ... (n*(n+1))/2
for i in range(l):
    for j in range(i+1,l+1):
        print(n[i:j])
