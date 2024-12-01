def diff(lst, result):
    if lst[0] == lst[1]:
        result = lst[2]
    elif lst[0] == lst[2]:
        result = lst[1]
    else:
        result = lst[0]
    return result

x_lst = []
y_lst = []
for tc in range(3):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)

x_result = 0
y_result = 0

print(f'{diff(x_lst, x_result)} {diff(y_lst, y_result)}')

# if x_lst[0] == x_lst[1]:
#     x_result = x_lst[2]
# elif x_lst[0] == x_lst[2]:
#     x_result = x_lst[1]
# else:
#     x_result = x_lst[0]
