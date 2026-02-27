def quickSort(a):
    if len(a)<=1:
        return a
    p = a[0]
    left = [x for x in a[1:] if x<=p]
    right = [y for y in a[1:] if y>p]
    return quickSort(left)+[p]+quickSort(right)
j = [25,37,11,14,60,82,18,41]
print(quickSort(j))
# def quick(a,left,right,loc):
#     while left < right:
#         while a[left] < a[loc]:
#             left+=1
#         a[left] , a[loc] = a[loc] , a[left]
#         loc = left
#         while a[right] > a[loc]:
#             right -= 1
#         a[right] , a[loc] = a[loc] , a[right]
#         loc = right
#     return left,right
# def QuickSort(a):
#     if len(a)<=1:
#         return a
#     p = a[0]
#     l,r= quick(a,0,len(a),0)
#     left = QuickSort(a[1:l])
#     right = QuickSort(a[r:-1])
#     return left+p+right
# j = [25,37,11,14,60,82,18,41]
# print(QuickSort(j))
def quick(a):
    if len(a) <= 1 : 
        return a
    p = a[0]
    left = [x for x in a[1:] if x<=p]
    right = [x for x in a[1:] if x>p]
    return quick(left)+[p]+quick(right)
j = [60,50,20,10,100,90,30]
print(quick(j)) 