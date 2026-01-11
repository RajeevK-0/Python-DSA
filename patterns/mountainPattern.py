N = int(input())
i = 1
while i<=N:
    k = 1
    while k<=i:
        print(k,end='   ')
        k+=1
    space = N-i
    k = 1
    while k<=space:
        print( '',end ='    ')
        k+=1
    space = N-i-1
    nums = N-1-space
    k = 1
    while k<= space:
        print( ' ', end =  '    ')
        k += 1
    if i==N:
        nums = N-1
        while nums!=0:
            print(nums,end='    ')
            nums-=1
    else:
        while nums!=0:
            print(nums,end='    ')
            nums-=1
    print()
    i+=1 