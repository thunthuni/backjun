# K: 랜선의 개수
# N: 필요한 랜선의 개수
# N 개를 만들 수 있는 랜선의 최대 길이는?
import sys

candidates = []

def isPossibleBy(l):
    cnt = 0
    for i in range(K):
        cnt += lans[i] // l

    return cnt >= N

def binarySearch(l, r):
    while l < r:
        m = (l + r) // 2
        if isPossibleBy(m):
            l = m + 1
        else:
            r = m
    return l


K, N = map(int, sys.stdin.readline().split())
lans = []
for _ in range(K):
    a = int(sys.stdin.readline())
    lans.append(a)

print(binarySearch(1, 2**31)-1)
