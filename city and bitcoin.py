# 오른쪽 또는 아래쪽
# 1은 갈 수 있고 0 은 못감
# 거래소 위치는 우하

# 어떻게 풀까?
# 현재 위치를 계속 업데이트 하면서 오, 아 방향이 1인지 확인
# 1이라면 스택에 넣기 => 방문할 곳을 저장하는 것
# 그렇게 탐색을 계속하다가 0이 나오면 마지막으로 1이 나왔던 곳으로 스택에서 pop 하면서 돌아오기
# 반복하다가 arr 의 [M-1][N-1]에 도착하게 되면 탐색 중단하고 Yes 출력
# 반복하다가 더이상 갈 수 있는 경로가 없으면 No 출력
# **진우의 초기 위치가 거래소일 수도 있음

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

# 방문할 곳들
q = [[0,0]]

# 진우의 초기위치
# r = 0
# c = 0

# 방향키
dr = [0, 1]  # 오, 아
dc = [1, 0]

# 탐색
while q:
    r, c = q.pop(0)

    if r == M-1 and c == N-1:
        print('Yes')
        break

    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 1:
            q.append((nr, nc))
            arr[nr][nc] = 2

else:
    print('No')



# 그니까 오른쪽이랑 아래쪽을 확인하는데 1이면
# 그 1인 위치에서 다시 오른쪽 아래쪽을 탐색하고
# 탐색을 계속 하다가 0 이 나와서 길이 막히게 되면 전에 방문 했던 갈래로 돌아와야 하는데
# 이거 어케함..다시 하나씩 돌아가야 하나
# 근데 이미 탐색해서 안된다고 파악한 곳은 표시를 해줘야 루프 안빠질듯 => 2 로 바꿔버리자
# 스택을 이용해서 내가 갔던 경로를 저장하자
# 그리고 막혀서 돌아갈 때는 2로 바꿔버리자

# 이러한 탐색을 arr[M-1][N-1]까지 갈 때동안 할 수 있냐 확인하자






