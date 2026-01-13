N= int(input())
def sumofDigits(N):
    sum = 0
    while N:
        sum+=N%10
        N //= 10
    return sum
print(sumofDigits(N))