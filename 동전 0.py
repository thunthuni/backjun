import sys

N, K = map(int, sys.stdin.readline().split()) # 동전의 단위 개수 , 맞춰야 하는 가격

coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline().rstrip()))

cnt = 0

for i in range(N, 0, -1):
    # if K // coins[i] >= 1:
    cnt += K // coins[i]
    K = K % coins[i]

print(cnt)

# 4 1 2 1 4
