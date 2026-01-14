N = int(input())
a = 0
b = 1
for i in range(N):
    print(a,end=' ')
    t = a
    a = b
    b += t