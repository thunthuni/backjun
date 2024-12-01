# 카드의 합이 21 을 넘지 않아야 함-> 21이하여야 함
# 카드의 합을 최대한 크게 만드는 게임
# 카드의 개수는 3

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if numbers[i] + numbers[j] + numbers[k] > M:
                continue
            else:
                result = max(result, numbers[i]+numbers[j]+numbers[k])
print(result)