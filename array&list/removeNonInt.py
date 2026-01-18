l = [1,'a',4,4.5,'bcd',5,6]
print(type(l[4]))
print(len(l))
print('before')
print(l)
print(type(l[0]))
if type(l[0]) == int:
    print('yes its int')
# this code will give problem cuz shift will be occuring as we remove i, so use either list comprehension or start from last i
# for i in l:
#     if type(i) != int:
#         l.remove(i)
l = [i for i in l if type(i)== int]
print('after')
print(l)
