# 1부터 N 까지 자연수 중에서 중복 없이 M개를 고른 수열
# 중복이 있어서는 안되고 각 수열은 공백으로 구분해서 출력
# 출력값은 오름차순으로 정렬

# **************** 풀이 ******************
# 백트래킹: DFS의 한 종류이지만 가지치기를 한다는 점이 다름
        # 모든 경우의 수를 탐색하는 대신 조건을 걸고 유망하지 않은 경우에
        # 탐색 중지하고 이전 노드로 돌아가서 다른 경우를 탐색


def dfs():
    if len(stack) == M:
        print(' '.join(map(str, stack)))
        return
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        stack.append(i)
        dfs()
        stack.pop()
        visited[i] = False


N, M = map(int, input().split())
stack = []
visited = [False] * (N+1)

dfs()


# BFS 탐색이랑 같은 것 같음
# 첫 시작점은 arr안에 숫자로 끝까지 업데이트 되는거고
# 그리고 그 시작점을 제외한 다른 숫자를 자식노드로 넣어주고
    # 그 자식노드를 제외한 다른 숫자를 자식노드로 넣어주고 사용한 숫자가 없을 때까지 반복































# subsets = [[]]
#
# for num in arr:
#     size = len(subsets)
#     for i in range(size):
#         subsets.append(subsets[i]+[num])
#
# print(subsets)
#
# for subset in subsets:
#     if len(subset) == M:
#         print(*subset)
#         # subset.reverse()
#         # print(*subset)

