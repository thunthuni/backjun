# A B C D
# 2 1 4 3

from collections import deque
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    # 문서의 개수, 몇 번째로 인쇄 되었는지 궁금한 문서의 큐 위에서의 위치
    N, M = map(int, sys.stdin.readline().split())
    importance = list(map(int, sys.stdin.readline().split()))
    documents = deque()
    order = [0] * N

    for i in range(N):
        documents.append((i, importance[i]))

    cnt = 0
    while cnt < N:
        max_v = max(importance)
        if documents[0][1] != max_v:
            documents.append(documents.popleft())
        else:
            cnt += 1
            order[documents[0][0]] += cnt
            documents.popleft()
            importance.remove(max_v)

    print(order[M])






