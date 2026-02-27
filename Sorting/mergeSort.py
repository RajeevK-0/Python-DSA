def merge(a,b):
    res = []
    while len(a)>0 and len(b)>0:
        if a[0]<b[0]:
            res.append(a.pop(0))
        else:
            res.append(b.pop(0))
    return res+a+b
def mergeSort(a):
    if len(a)<= 1:
        return a
    mid = (len(a))//2
    l = mergeSort(a[:mid])
    r = mergeSort(a[mid:])
    return merge(l,r)
j = [60,50,20,10,100,90,30]
print(mergeSort(j))


def mSort(a):
    if len(a)>1:
        mid = len(a)//2
        left = mSort(a[:mid])
        right = mSort(a[mid:])
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i+=1
                k+=1
            else:
                a[k] = right[j]
                j+=1
                k+=1
        while i< len(left):
            a[k] = left[i]
            i+=1
            k+=1
        while j< len(right):
            a[k] = right[j]
            j+=1
            k+=1
    return a
j = [60,50,20,10,100,90,30]
print(mSort(j))