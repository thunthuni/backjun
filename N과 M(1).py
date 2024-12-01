# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 중복되는 수열을 여러 번 출력하면 안됨

N, M = map(int, input().split())
visited = [False] * (N+1)
q = []


def permutation():
    if len(q) == M:
        print(*q)
        return
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            q.append(i)
            permutation()
            q.pop()
            visited[i] = False

permutation()