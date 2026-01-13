N= int(input())
for i in range(N):
    for j in range(N-i):
        print(' ',end='')
    if i == 0 or i == N-1:
        st = N*'*'
        print(st,end='')
    for j in range(N):
        if j == 0 or j == N-1:
            if i == 0 or i == N-1:
                continue
            else:    
                print('*',end='')
        else:
            print(' ',end='')
    print()   




# i = 1
# lspace = 1
# while i<=N:
#     lspace = N-i
#     j=1
#     while j<=lspace:
#         print(' ' , end='')
#         j+=1
#     j = 1
#     if i == 1 or i == N:
#         while j<=N:
#             print('*',end='')
#             j +=1
#     else :
#         while j<=N:
#             if j == 1 or j == N:
#                 print('*' , end = '')
#             else :
#                 print(' ', end = '')
#             j+=1
#     print()
#     i+=1