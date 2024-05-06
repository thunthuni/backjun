N = int(input())

dp = [[1, 1], [1, 2], [2, 1], [3, 1], [2, 2], [3, 1]]
        # 0       1      2        3       4      5

for i in range(6, N+1):
    temp = [0,0]
    if i % 2 == 0:
        temp[0] += dp[-3][0] + 1
        temp[1] += dp[-3][1]
    else:
        temp[1] += dp[-2][1] + 1
        temp[0] += dp[-2][0]
    dp.append(temp)

print(dp[N-1])
