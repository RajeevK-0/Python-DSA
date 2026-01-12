N = int(input())
mid = N//2
max = mid+1
for i in range(-mid,mid+1):
    row = abs(i)
    sp = 2*row
    for t in range(sp,0,-1):
        print(' ',end='    ')
    k = max-row
    for t in range(k , 0, -1):
        print(t,end='    ')
    midsp = 2*(mid-row)-1
    for t in range(midsp):
        print(' ',end='    ')
    if row!= mid:
        for t in range(1,k+1):
            print(t,end='    ')
    print()