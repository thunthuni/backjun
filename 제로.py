# 설탕 N 킬로 배달해야 됨
# 봉지는 3, 5
# 설탕봉지 개수 최소로

import sys

N = int(sys.stdin.readline())

nums = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num > 0:
        nums.append(num)
    else:
        nums.pop()
print(sum(nums))