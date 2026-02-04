def oddSum(N):
    if N == 1:
        return 1
    return oddSum(N-1)+2*N-1
print(oddSum(5))