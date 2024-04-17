alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

lst = input()
cnt = 0
for al in alpha:
    if al in lst:
        cnt += lst.count(al)
