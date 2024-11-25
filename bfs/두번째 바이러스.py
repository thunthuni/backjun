N = int(input())
M = int(input())

lst = [[] for _ in range(N+1)]
visited = [0] * (N+1)
q = [1]
num = -1
for i in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
print(lst)
# q가 빌때까지
while len(q) > 0:
    value = q.pop(0)
    if visited[value] == 0:
        q.extend(lst[value])
        visited[value] = 1
        num += 1

print(num)


