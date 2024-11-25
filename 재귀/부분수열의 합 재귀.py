

# 구해야 하는 값: 합이 S가 되는 부분수열의 개수

def recur(k, n):
    global totalN
    if k == n:
        # print(b)
        sum_value = 0
        for i in range(N):
            if b[i] == 1:
                sum_value += nums[i]
        # print(sum_value)
        if sum_value == S:
            totalN += 1
    else:
        b[k] = 0
        recur(k+1, n)
        b[k] = 1
        recur(k+1, n)


N, S = map(int, input().split())
nums = list(map(int, input().split()))
# N = 3
# S = 3
# nums = [1, 2, 3]

b = [0] * N
if S == 0:
    totalN = -1
else:
    totalN = 0
recur(0, N)

print(totalN)