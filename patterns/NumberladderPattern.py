N = int(input())
i = 1
k = 1
while i<=N:
    t = 1
    while t<=i:
        print(k,end='   ')
        k+=1
        t+=1
    print(' ')
    i += 1