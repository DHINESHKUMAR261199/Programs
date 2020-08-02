import numpy
n,m=map(int,input().split())
DW=numpy.zeros((n+2,n+2))
DW[0][n+1]=1
for i in range(n,m-1,-1):
    for j in range(n+1):
        DW[j][i]=DW[j][i+1]
        if j-i>=0:
            DW[j][i]=DW[j][i]+DW[j-i][i]
print(int(DW[n][m]))
