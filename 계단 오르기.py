# 규칙
# 계단은 한번에 한 계단 or 두 계단
# 연속된 세계의 계단을 모두 밟으면 안됨 but 시작점은 계단에 포함 노
# 마지막 도착 계단은 반드시 밟아야 됨

import sys

# 구해야 하는 값: 합의 최대값



N = int(sys.stdin.readline())
stairs = []
sum_v = 0
for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

b = [0] * N
