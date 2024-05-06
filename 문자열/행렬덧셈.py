import sys
N, M = map(int,input().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = []
for r in range(N):
    temp = []
    for c in range(M):
        temp.append(A[r][c] + B[r][c])
    result.append(temp)

for i in range(N):
    print(*result[i])