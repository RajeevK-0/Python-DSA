l = [1,'a',4,4.5,'bcd',5,6]
print(type(l[4]))
print(len(l))
print('before')
print(l)
print(type(l[0]))
if type(l[0]) == int:
    print('yes its int')
for i in l:
    if type(i) != int:
        l.remove(i)
print('after')
print(l)
