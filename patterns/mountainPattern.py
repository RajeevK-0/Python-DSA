N = int(input())
for i in range(N):
    row = i
    for j in range(i+1):
            print(j+1,end='    ')
    space = 2*(N-i-1)-1
    for k in range(space):
        print(' ',end='    ')
    t = row+1
    while t:
        if t == N:
            t-=1
            continue
        else:
            print(t,end='    ')
            t-=1
    print()


# i = 1
# while i<=N:
#     k = 1
#     while k<=i:
#         print(k,end='   ')
#         k+=1
#     space = N-i
#     k = 1
#     while k<=space:
#         print( '',end ='    ')
#         k+=1
#     space = N-i-1
#     nums = N-1-space
#     k = 1
#     while k<= space:
#         print( ' ', end =  '    ')
#         k += 1
#     if i==N:
#         nums = N-1
#         while nums!=0:
#             print(nums,end='    ')
#             nums-=1
#     else:
#         while nums!=0:
#             print(nums,end='    ')
#             nums-=1
#     print()
#     i+=1 