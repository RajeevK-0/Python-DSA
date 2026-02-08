def printN(N):
    if N <=0:
        return
    print(N)
    printN(N-1)
printN(5)