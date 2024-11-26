import sys

N = int(sys.stdin.readline())
positive = [0] * (1000001)
negative = [0] * (1000001)
negative_is = False

for _ in range(N):
    n = int(sys.stdin.readline())
    if n >= 0:
        positive[n] = 1
    else:
        negative_is = True
        negative[abs(n)] = 1

if negative_is:
    for i in range(1000000, 0, -1):
        if negative[i]:
            print(f'-{i}')
for i in range(1000001):
    if positive[i]:
        print(i)
