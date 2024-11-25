
T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * N for _ in range(M)]
    q = []
    for _ in range(K):
        r, c = map(int, input().split())
        # if not q:
        #     q.append((r, c))
        arr[r][c] = 1

    # 방향키 설정
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    worm = 0

    # q가 빌 때까지
    def count_worm():
        global worm

        # q가 빌 때까지
        while q:
            r, c = q.pop(0)
            arr[r][c] = 2
            # 1인곳을 찾아서
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 1:
                    q.append((nr, nc))
                    arr[nr][nc] = 2
        worm += 1


    for row in range(M)\
            :
        for col in range(N):
            if arr[row][col] == 1:
                r = row
                c = col
                q.append((r, c))
                arr[r][c] = 2
                count_worm()

    print(worm)



# 이거 위치 잘못됨 -> 이렇게 되면 처음에 시작점 (0,0) + 1, 주변 위치 탐색하면서 +1 이 됩니다. 또한 모든 위치를 한번씩 탐색해야만 지역별로 나눌 수 있을 것으로 예상 됩니다. 31번, 32번을 활용하면 좋을 것 같습니다.