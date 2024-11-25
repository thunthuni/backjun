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
