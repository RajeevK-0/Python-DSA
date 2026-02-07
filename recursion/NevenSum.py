def evenSum(N):
    if N == 0:
        return 0
    return evenSum(N-1)+2*N
print(evenSum(5))