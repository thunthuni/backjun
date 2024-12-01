# 0 : 2*2
# 1: 3
# 2: 5
# 3: 9
# 4: 17
# 5: 33

N = int(input())
dp = [2, 3, 5, 9, 17, 33]
for i in range(6, N+1):
    dp.append(dp[i-1]*2-1)

print(dp[N]**2)