# N = int(input())
# dp = [0] * (N+1)
# dp[0], dp[1] = 0, 4
#
# for i in range(2, N+1):
#     dp[i] = dp[i-1] + 4
# print(dp[N])

N = int(input())
print(N*4)