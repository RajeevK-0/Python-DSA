N = 10
l = []
k = 2
while len(l)<N:
    for j in range(2,int((k**0.5))+1):
        if k%j == 0:
            break
    else:
        l.append(k)
    k+=1          
print(l)
