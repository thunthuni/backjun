# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
import sys

def dfs():
    if len(stack) == M:
        return

    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        stack.append(i)
        dfs()
        stack.pop()


N, M = map(int, sys.stdin.readline().split())
stack = []

visited = [False] * (N+1)
