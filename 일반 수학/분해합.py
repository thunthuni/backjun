N = int(input())

candi = []
for num in range(1, N+1):
    sum_v = 0
    lst = str(num)
    for i in range(len(lst)):
        sum_v += int(lst[i])
    if num + sum_v == N:
        candi.append(num)
if len(candi) > 0:
    print(min(candi))
else:
    print(0)

# 다른 사람의 코드
N = int(input())

for i in range(1, N + 1):
    digits_sum = i + sum(map(int, str(i)))
    if digits_sum == N:
        print(i)
        break
else:
    print(0)
