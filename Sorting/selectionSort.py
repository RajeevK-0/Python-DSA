def selectionSort(a):
    for i in range(len(a)-1):
        p = i
        for j in range(i+1,len(a)):
            if a[j] < a[p]:
                p = j
        a[i] , a[p] = a[p] , a[i]
    return a
j = [10,30,20,9,25]
print(selectionSort(j))