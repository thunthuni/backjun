# N개의 강의
# 서로 연결된 건물들을 찾아야 됨
# 떨어진 건물 개수 찾으면 될 듯
import sys


def find(n):
    if parents[n] < 0:
        return n
    parents[n] = find(parents[n])
    return parents[n]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parents[b] = a


N, M = map(int, sys.stdin.readline().split())
parents = [-1] * (N+1)  # 부모 초기화
count = 0
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)

classes = list(map(int, sys.stdin.readline().split()))

roots = []
for c in classes:
    roots.append(find(c))

for i in range(1, N):
    if roots[i] != roots[i-1]:
        count += 1

print(count)


