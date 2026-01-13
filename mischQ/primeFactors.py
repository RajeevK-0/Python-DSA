N = int(input())
def primeFactors(N)->list:
    l = []
    a = 2 
    while N>1:
        while N%a == 0:
            l.append(a)
            N //= a
        a+=1
    return l
print(primeFactors(N),end='')