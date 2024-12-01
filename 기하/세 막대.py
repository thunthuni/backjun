lst = sorted(list(map(int, input().split())))
if lst[0] + lst[1] > lst[2]:
    print(sum(lst))
else:
    print((lst[0]+lst[1])*2 - 1)
# 작은 두수의 합이 가장 큰 수보다 크다면 전체의 합
# 작다면 작은 두수의 합의 두배에서 1을 뺀 값

