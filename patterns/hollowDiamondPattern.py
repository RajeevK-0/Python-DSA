n = int(input())
mid = n // 2

for i in range(n):
    for j in range(n):
        d = abs(i - mid) + abs(j - mid) 
        if d<mid:
            print(" ", end="    ")
        else:
            print("*", end="    ")
    print()