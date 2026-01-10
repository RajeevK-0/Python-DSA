N = int(input())
i = 1
while i <= N:
    space = i-1
    j = 1
    while j<=space:
        print(' ',end=' ')
        j+=1
    t = N-i+1
    while t != 0:
        print(t, end=' ')
        t-=1
    print('0',end = ' ')
    t = N-i+1
    k = 1
    while k<=t:
        print(k,end = ' ')
        k+=1
    i+=1
    print()
i = 1
while i<=N:
    if i == N:
        print('  0',end=' ')
    else:    
        print(' ',end = ' ')
    i+=1
print()
i = 1
while i <= N:
    space = N-i
    k = 1
    while k<=space:
        print(' ',end = ' ')
        k+=1
    num = N - space
    while num !=0:
        print(num,end=' ')
        num -= 1
    print('0',end=' ')
    k = 1
    while k<=i:
        print(k, end=' ')
        k+=1 
    i+=1
    print()
