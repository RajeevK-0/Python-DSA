N = int(input())
mid = N//2
for i in range(N):
    for j in range(N):
        s = abs(mid-i)+abs(mid-j)
        if s <=mid:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()     