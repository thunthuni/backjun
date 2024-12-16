import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

prefix = [0] * (N+1)
for i in range(1, N+1):
    prefix[i] = prefix[i-1] + numbers[i-1]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())

    print(prefix[j] - prefix[i-1])
