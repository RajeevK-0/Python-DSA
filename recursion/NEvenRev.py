def revEven(N):
    if N<=0:
        return
    print(2*N,end=' ')
    revEven(N-1)
revEven(5)