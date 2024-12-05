# 산술평균 (소수점 이하 첫째 자리에서 반올림한 값)
# 중앙값 ( n// 2 인덱스에 위치 한 값)
# 최빈값 (여러 개일시 최빈값 중 두번째로 작은 값)
# 범위 ( max - min)
import sys

numbers = [0] * 8001
lst = []
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    lst.append(num)

lst.sort()

before = lst[0]
cnt = 0
for n in lst:
    if n != before:
        numbers[before + 4000] = cnt
        cnt = 1
        before = n
    else:
        cnt += 1
        numbers[before + 4000] = cnt

max_v = max(numbers)
modes = []
for i in range(8001):
    if numbers[i] == max_v:
        modes.append(i - 4000)

print(round(sum(lst)/N))
print(lst[N//2])
if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])
print(max(lst) - min(lst))