from array import *
a1 = array('i',[1,2,3,4,5,6,7,8])
print(type(a1))
for i in range(len(a1)):
    print(a1[i],end=' ')
print(a1.count(5))
import numpy as np
a = np.array([1,2,3,4,5,6])
print(len(a))