import sys

# 도시 개수 N
# 두 도시 사이에 길이 있? 없?
# 여행 일정에 따라서 여행 경로가 가능?

def find(n):
    if parents[n] < 0:
        return n
    parents[n] = find(parents[n])
    return parents[n]


def union(a, b):
    A = find(a)
    B = find(b)

    if A != B:
        parents[B] = A


N = int(sys.stdin.readline()) # 도시의 수
M = int(sys.stdin.readline()) # 여행계획에 속한 도시 수
# connected = [[] for _ in range(N+1)]
parents = [-1]*(N+1)

for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if lst[j] == 1:
            # connected[i+1].append(j+1)
            union(i+1, j+1)

cities = list(map(int, sys.stdin.readline().split()))

roots = []
for i in range(M):
    roots.append(find(cities[i]))

# print(roots)
if len(set(roots)) == 1:
    print('YES')
else:
    print('NO')