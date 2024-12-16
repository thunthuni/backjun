import sys

N = int(sys.stdin.readline())
if N == 0:
    factorial = 0
else:
    factorial = 1

for i in range(1, N+1):
    factorial = factorial * i

str_fact = str(factorial)
zero_cnt = 0

for i in range(len(str_fact)-1, 0, -1):
    if str_fact[i] == '0':
        zero_cnt += 1
    else:
        break

print(zero_cnt)