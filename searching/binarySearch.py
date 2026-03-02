def binary(l1,x,l,u):
    mid = (u+l)//2
    if l>u:
        return -1
    if x == l1[mid]:
        return mid
    if x < l1[mid]:
        return binary(l1,x,u,mid-1)
    if x > l1[mid]:
        l = mid+1
        return binary(l1,x,mid+1,u)