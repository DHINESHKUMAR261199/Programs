t=int(input())
for _ in range(t):
    board=[]
    N,M=map(int,input().split())
    for i in range(N):
        board.append(list(map(int,input().split())))
    white=[]
    for i in board:
        temp=[]
        for p,v in enumerate(i,1):
            if v:
               temp.append(p)
        white.append(temp)
    print(white)
    c=len(white[0])
    max1=0
    for i in range(N-1):
        if white[i][0]-1 in white[i+1] or white[i][-1]+1 in white[i+1]:
            c+=len(white[i+1])
            print(c)
        else:
            max1=max(c,max1)
            c=0
    print(max1)
