# 나이 오름차, 같으면 먼저 가입한 사람

import sys

N = int(sys.stdin.readline())
lst = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    lst.append((int(age), name, i))

lst.sort(key = lambda x: (x[0], x[2]))

for i in lst:
    print(*i[0:2])