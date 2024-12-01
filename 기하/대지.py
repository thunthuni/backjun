T = int(input())
# n = int(sys.stdin.readline().strip())
x_lst = []
y_lst = []
for tc in range(T):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)

print((max(x_lst)-min(x_lst))*(max(y_lst)-min(y_lst)))