def bubbleeSort(a):
    n = len(a)
    for k in range(n):
        for i in range(n-k):
            if i < n-1:
                j = i+1
                if a[i] > a[j]:
                    t = a[i]
                    a[i] = a[j]
                    a[j] = t
    return a
j = [10,30,20,9,25]
print(bubbleeSort(j))