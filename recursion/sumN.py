def sum(N):
    if N==1:
        return 1
    return sum(N-1)+N
print(sum(5))