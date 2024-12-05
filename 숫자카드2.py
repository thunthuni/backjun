import sys

N = int(sys.stdin.readline()) # 숫자카드의 개수
numbers = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline()) # 몇 개인지 구해야 하는 카드의 개수
have_numbers = list(map(int, sys.stdin.readline().split()))

cnt_negative = [0] * 10000001
cnt_positive = [0] * 10000001

for num in numbers:
    if num < 0:
        cnt_negative[num] += 1
    else:
        cnt_positive[num] += 1

result = []
for num in have_numbers:
    if num < 0:
        result.append(cnt_negative[num])
    else:
        result.append(cnt_positive[num])

print(*result)