# 친구 관계가 생긴 순수대로 주어짐
# 두 사람의 친구 네트워크에 몇명이 있는지?
# 친구 네트워크: 친구 관계만으로 이동할 수 있는 사이
import sys


def find(n):  # root 를 찾는 함수쨩
    if parents[n] == n:  # 만약 루트가 자기 자신이라면?
        return parents[n]  # 자기 자신을 리턴
                        # 아니라면?
    parents[n] = find(parents[n])  # 부모의 부모는 부모입니다
    return parents[n]


def union(a, b):
    A = find(a)
    B = find(b)

    if A != B:
        # temp = parents[B]
        parents[B] = A
        # for key, value in parents.items():
        #     if value == temp:
        #         parents[key] = A


T = int(sys.stdin.readline())
for tc in range(T):
    F = int(sys.stdin.readline())
    friends = []
    parents = {}
    for _ in range(F):
        a, b = sys.stdin.readline().split()
        if a not in friends:
            friends.append(a)
            parents[a] = a
        if b not in friends:
            friends.append(b)
            parents[b] = b
        union(a, b)

        count = list(parents.values()).count(find(a))
        print(count)
