def NEven(N):
    if N<=0:
        return
    NEven(N-1)
    print(2*N,end=' ')
NEven(5)