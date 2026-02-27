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