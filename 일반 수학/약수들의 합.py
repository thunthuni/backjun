import sys
sys.stdin = open('../input.txt')

while True:
    N = int(input())
    if N == -1:
        break
    lst = []
    for i in range(2, N):
        if N % i == 0:
            lst.append(i)
    if sum(lst) + 1 == N:
        result = '1'
        for i in lst:
            result += ' + '
            result += str(i)
        print(f'{N} = {result}') 
    else: 
        print(f'{N} is NOT perfect.')
    