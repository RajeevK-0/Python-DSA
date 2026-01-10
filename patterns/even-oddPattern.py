N= int(input())
i = 1
while i<=N:
    if i %2 != 0:
        one = i*'1'
        print(one,end='')
    else:
        j = 1
        while j<=i:
            if j == 1 or j == i:
                print('1',end='')
            else:
                print('0',end='')
            j+=1
    print()
    i+=1
    
