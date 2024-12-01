<<<<<<< HEAD
# 한거번에 생각하려고 하지 말자
# 지금 내가 헷갈려 하는 것은 8*8 을 어떻게 다 확인할 것인가 
# 먼저 c 0-8 까지 갔다가 
# r은 그대로 c +1 해서

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

min = 1
num = 0 
r = 0
c = 0 

for r in range(N-7):
    for c in range(M-7):
        for i in range(r, r+8):
            for j in range(c, c+7):
                if arr[i][j] == arr[i][j+1]:
                    arr[i][j+1] = 1
                    num += 1
        if num < min:
            min = num
    
        
print(min)
=======
# 다시 칠해야 하는 정사각형 개수의 최솟값

import sys

M, N = map(int, sys.stdin.readline().split())
board = [list(str(sys.stdin.readline()).strip('\n')) for _ in range(M)]

print(board)
min_v = 10000000000000

for r in range(M-7):
    for c in range(N-7):
        cnt = 0
        new_board = ''
        new_board += board[r][c]
        for i in range(r, r+8):
            for j in range(c+1, c+8):
                if new_board[-1] == 'B' and board[i][j] == 'B':
                    cnt += 1
                    new_board += 'W'
                elif new_board[-1] == 'W' and board[i][j] == 'W':
                    cnt += 1
                    new_board += 'B'
                else:
                    new_board += board[i][j]
        if min_v > cnt:
            min_v = cnt

print(min_v)
>>>>>>> c1d296daa1f39c381a18541154e57df0857ce78c
