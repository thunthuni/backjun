# 3킬로 / 5킬로 봉지 최소개수
# 정확하게 N킬로 못만들면 -1

import sys

N = int(sys.stdin.readline())

# result = 0
# min_v = 100000000
#
# for i in range(N//5 + 1):  # 5킬로 봉지 개수
#     for j in range(N//3 + 1):  # 3킬로 봉지 개수
#
#         if (5 * i) + (3 * j) == N:
#             if (i+j) < min_v:
#                 min_v = i + j
#
# if min_v == 100000000:
#     result = -1
# else:
#     result = min_v
#
# print(result)


result = 0
is_possible = False
while N >= 0:
    if N % 5 == 0:
        result += N // 5
        print(result)
        is_possible = True
        break
    N -= 3
    result += 1

if not is_possible:
    print(-1)
