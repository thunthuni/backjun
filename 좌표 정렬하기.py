import sys

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

lst.sort(key = lambda x: (x[0], x[1]))

for _ in lst:
    print(*_)