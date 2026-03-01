def binary(l1,x):
    l = 0
    u = len(l1)-1
    mid = (u+l)//2
    if x == l1[mid]:
        return mid
    if x < l1[mid]:
        u = mid-1
        binary(l1[:u],x)
    if x > l1[mid]:
        l = mid+1
        binary(l1[l:],x)