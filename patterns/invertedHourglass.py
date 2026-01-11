N = int(input())
for i in range(-(N),N+1):
    row = abs(i)
    space = 2*row -1
    n = N
    while n >= row:
        print(n,end=' ')
        n-=1
    i = 1
    while i<=space:
        print(' ', end=' ')
        i+=1 
    n = N
    e = row or 1
    while n >=e:   
        print(e,end=' ')
        e+=1
    print()


#brute force
# N = int(input())
# i = 1
# while i <=2*N+1:
#     if i<=N:
#         sp = N-i+1
#         k = N
#         j = 1
#         while j<=i:
#             if j == N:
#                 print(k,end= '') 
#                 k-=1
#                 j+=1  
#             else:
#                 print(k,end= ' ')
#                 k-=1
#                 j+=1
#         while sp!=0:
#             print(' ',end=' ')
#             sp-=1
#         sp = N-i
#         k = N-i+1
#         while sp!=0:
#                 print(' ',end=' ')
#                 sp -= 1
#         j = 1
#         if i == N:
#             print('',end=' ')
#         while j<=i:
#             while k != N+1:
#                 print(k,end= ' ')
#                 k+=1
#             j+=1
#     elif i==N+1:
#         k =  N
#         while k!=0:
#             print(k,end=' ')
#             k-=1
#         print('0' , end = ' ')
#         t = 1
#         while t<=N:
#             print(t,end=' ')
#             t+=1
#     else:
#         space = i-N-1
#         count = N+1 -space
#         j = 1
#         n = N
#         while j<=count:
#             print(n,end=' ')
#             n -= 1
#             j += 1
#         while space!=0:
#             print(' ',end=' ')
#             space-=1
#         space = i-N-2
#         while space!=0:
#             print(' ',end=' ')
#             space-=1
#         k = 1
#         sp = i-N-1
#         while sp<=N :
#             print(sp,end=' ')
#             sp+=1 
#     i+=1
#     print()