n = int(input())
mid = n // 2

for i in range(n):
    for j in range(n):
        if (
            i == 0 or i == n-1 or j == 0 or j == n-1 or
            abs(i - mid) + abs(j - mid) == mid
        ):
            print("*", end="    ")
        else:
            print(" ", end="    ")
    print()