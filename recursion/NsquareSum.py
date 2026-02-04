def squareSum(N):
    if N == 1:
        return 1
    return squareSum(N-1)+N**2
print(squareSum(3))