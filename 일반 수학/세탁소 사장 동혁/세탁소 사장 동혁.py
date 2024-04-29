import sys
sys.stdin = open('input.txt')
T = int(input())
coins = [25, 10, 5, 1]
for _ in range(T):
    counts = [0, 0, 0, 0]
    N = int(input())
    for i in range(4):
        coin = coins[i]
        if coin <= N:
            counts[i] += N // coin
            N = N%coin
    print(*counts)