import sys


def dfs():
    if len(stack) == M:
        temp = stack.copy()
        temp.sort()
        if temp not in stacks:
            print(' '.join(map(str, temp)))
            stacks.append(temp)
        return

    for i in range(1,  N+1):
        if visited[i]:
            continue
        visited[i] = True
        stack.append(i)
        dfs()
        stack.pop()
        visited[i] = False


N, M = map(int, sys.stdin.readline().split())

stack = []
stacks = []
visited = [False] * (N+1)

dfs()
print(' '.join(map(str, stack)))

