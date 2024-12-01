import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())  # 컵의 개수 & 컵을 옮기는 동작의 수
    cups = list(map(int, input().split()))

    moves = []  # 컵을 옮기는 동작
    adj = [[] for i in range(N + 1)]  # 인접한 노드
    counts = cups.copy()  # 컵에 몇개 있는지 => answer

    for _ in range(M):
        moves.append(list(map(int, input().split())))

    for i in range(M):
        adj[moves[i][1]].append(moves[i][0])

    stack = []  # 방문할 노드를 저장
    visited = []  # 방문한 노드를 저장
    # stack.extend(adj[1])  # 탐색 시작 노드들 넣기 stack = [2, 4]
    # visited.extend(adj[1])  # 탐색 시작 노드 방문 처리 visited = [2, 4]

    # 모든 노드를 방문할 때까지
    while stack:
        temp = stack.pop(-1)
        if adj[temp]

        # if adj[i]:
        #     for j in range(len(adj[i])):
        #         counts[i] += cups[adj[i][j]]
        #         if adj[adj[i][j]]:
