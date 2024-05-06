N = int(input())
result = 0
# 1 - 7       6
# 8 - 19     12
# 20 - 37    18
# 38- 61     24
if N == 1:
    result = 1

if result != 1:
    dp = [0, 7, 19]
    while dp[-1] <= N:
        dp.append(dp[-1] + (dp[-1]-dp[-2]+6))

    lenn = len(dp)
    for i in range(lenn):
        if i + 1 < lenn:
            if N in range(dp[i]+1, dp[i+1]+1):
                result = i+2
print(result)
