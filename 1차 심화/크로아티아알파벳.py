alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

lst = input()
# cnt = 0
# for al in alpha:
#     if lst.count(al) > 0:
#         n = lst.count(al)
#         if len(al) == 2:
#             cnt += 1*n
#         else:
#             cnt += 2*n - n
# print(len(lst) - cnt)

############### 남의 코드
for i in alpha:
    if i in lst:
        lst = lst.replace(i, '!')
print(lst)
print(len(lst))