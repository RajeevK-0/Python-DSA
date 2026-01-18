N = 10
l = []
a = 0
b = 1
while len(l)<N:
    t = a
    a = b
    b = a+t
    l.append(a)
print(l)