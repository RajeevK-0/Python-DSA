N = int(input())
mid = N-1
for i in range(-mid , mid+1):
    row = abs(i)
    for j in range(-mid , mid+1):
        col = abs(j)
        s = abs(mid-row)+abs(mid-col)
        if s > mid:
            print(" ",end='')
        else:
            print('*',end='')
    print()






# i = 0
# while i < 2*N-1:
#     if i == 0 or i == 2*N-2:
#         stars = (2*N-1) *'*'
#         print(stars)
#     else:
#             if i<N:
#                 stars = (N - i)*'*'
#                 space = (2*i-1)*' '
#                 s = stars+space+stars
#                 print(s)
#             else:
#                 j = i-N+2
#                 stars = j*'*'
#                 space = ((2*N -1)-2*j)*' '
#                 s = stars+space+stars
#                 print(s)
#     i+=1