# a층의 b호에 sum(아래층 1호 ~ b호)
# k 층 n 호에 몇 명 살고 있음?

import sys
input = sys.stdin.readline

T = int(input())
dp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

for _ in range(T):
    K = int(input())  # 층
    N = int(input())  # 호

    index = 14 * K + N
    if len(dp) < index:
        for i in range(len(dp), index + 1):
            if i % 14 == 1:
                dp.append(1)
            else:
                dp.append(dp[-1] + dp[i - 14])

    print(dp[index])

