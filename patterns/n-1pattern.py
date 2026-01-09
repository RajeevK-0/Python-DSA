N = int(input())
i = 1
j = 1
while i <= N:
    if i == 1:
        print(i , end = '')
    else:
        t = 1
        j = i - 1
        while t <= i:
            if t == 1 or t== i:
                print(j , end='')
            else:
                print('0',end='')
            t+=1
    print()
    i+=1
    