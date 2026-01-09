N = int(input())
a = 0
b = 1
i = 1
while i<=N:
    j = 1
    while j <=i:
        print(a,end = ' ')
        temp = a
        a = b
        b = temp + b
        j+=1
    i+=1 
    print()