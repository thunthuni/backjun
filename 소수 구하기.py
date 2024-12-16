# M 이상 N 이하의 소수를 모두 출력
import sys
M, N = map(int, sys.stdin.readline().split())

num_lst = [True] * 1000001
num_lst[1] = False
for num in range(2, N+1):  # N+1-M
    if not num_lst[num]:
        continue
    k = 2
    while num*k < N+1:
        num_lst[num*k] = False
        k += 1
    
for i in range(M, N+1):
    if num_lst[i]:
        print(i)

