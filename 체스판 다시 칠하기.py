# 다시 칠해야 하는 정사각형 개수의 최솟값

import sys

M, N = map(int, sys.stdin.readline().split())
board = [list(str(sys.stdin.readline()).strip('\n')) for _ in range(M)]

cnt = []

for r in range(M-7):
    for c in range(N-7):
        wi = 0
        bi = 0
        for i in range(r, r+8):
            for j in range(c, c+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        wi += 1
                    else:
                        bi += 1
                else:
                    if board[i][j] != 'W':
                        bi += 1
                    else:
                        wi += 1
        cnt.append(wi)
        cnt.append(bi)

print(min(cnt))
