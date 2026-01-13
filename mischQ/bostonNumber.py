N= int(input())
def sumOfDigits(n):
    sum = 0 
    while n:
        sum += n%10
        n //= 10
    return sum
def primeFactorsSum(n):
    a = 2
    sum = 0 
    
    while n>1:
        while n%a==0:
            sum+= sumOfDigits(a)
            n //= a
        a+=1
    return sum

def isBoston(N):
    return primeFactorsSum(N) == sumOfDigits(N)

print(isBoston(N))
for i in range(100):
    if isBoston(i):
        print(i)
