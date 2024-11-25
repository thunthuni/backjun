import sys

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

result = []

for i in range(N):
    weight = lst[i][0]
    height = lst[i][1]
    new_lst = lst.copy()
    new_lst.pop(i)
    cnt = 0
    for j in range(N-1):
        if new_lst[j][0] > weight and new_lst[j][1] > height:
            cnt += 1
    result.append(cnt + 1)

print(*result)