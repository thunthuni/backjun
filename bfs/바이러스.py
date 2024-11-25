
N = int(input())
M = int(input())
lst = [[] for _ in range(N+1)]
visited = [0] * (N+1)

num = -1
q = [1]
for i in range(M):
    a, b = map(int, (input().split()))
    lst[a].append(b)
    lst[b].append(a)

while len(q) > 0:
    temp = q.pop(0)
    if visited[temp] == 0:
        q.extend(lst[temp])
        visited[temp] = 1
        num += 1
    # else:
    #     q.pop(0)

print(num)












