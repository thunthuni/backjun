import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())  # 컵의 개수 & 컵을 옮기는 동작의 수
    cups = list(map(int, input().split()))
    moves = []  # 컵을 옮기는 동작
    for _ in range(M):
        moves.append(list(map(int, input().split())))

    for i in range(M):
        from_cup = moves[i][0] - 1
        to_cup = moves[i][1] - 1
        cups[to_cup] += cups[from_cup]

    print(cups)