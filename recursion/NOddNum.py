def printOdd(N):
    if N<=0:
        return
    printOdd(N-1)
    print(2*N-1,end=' ')
printOdd(6)
    
