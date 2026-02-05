def printN(N):
    if N <= 0:
        return
    printN(N-1)
    print(N)
printN(6)

