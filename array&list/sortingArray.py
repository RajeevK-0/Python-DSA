from array import *
a = array('i', [2,1,3,2,4,3,6,33,7,6])
#sort this array
l = len(a)
for i in range(l):
    for j in range(i+1,l):
        if a[i]>a[j]:
            # t = a[i]
            # a[i] = a[j]
            # a[j] = t
            a[i],a[j] = a[j],a[i]
b = sorted(a)
print(sorted(a))
print(b)
print(a)