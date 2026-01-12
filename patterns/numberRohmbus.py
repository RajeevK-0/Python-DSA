N = int(input())
for i in range(-(N-1),N):
    row = abs(i)
    for j in range(row+1):
        print(' ',end='    ')
    t = N-row
    for j in range(1,(N-row)+1):
        print(t,end='    ')
        t = t+1   
    for k in range(t-2,N-row-1,-1):
        print(k,end='    ')
    print()
