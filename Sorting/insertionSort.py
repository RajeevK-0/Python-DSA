def insertionSort(a):
    n = len(a)
    for i in range(n):
        k = i
        t = i
        while k >=0 :
            if a[k] > a[t]:
                a[k] , a[t] = a[t],a[k]
                t = k
            k-=1
    return a
j = [10,30,20,9,25]
print(insertionSort(j))

def insrtSort(a):
    for i in range(1,len(a)):
        t = a[i]
        j = i-1
        while j>=0 and t<a[j]:
            a[j+1] = a[j]
            j-=1
        a[j+1] = t
    return a
j = [25,37,11,14,60,82,18,41]
print(insrtSort(j))