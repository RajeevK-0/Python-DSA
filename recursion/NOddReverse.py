def revOdd(N):
    if N<=0:
        return
    print(2*N-1,end=' ')
    revOdd(N-1)
revOdd(6)