import sys
N = int(sys.stdin.readline())

k = [0] * 100_00
for i in range(N):
    k[int(sys.stdin.readline())] += 1

for i in range(1, 100000):
    if k[i] != 0:
        for _ in range(k[i]):
            print(i)

