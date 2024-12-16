import sys

N, M = map(int, sys.stdin.readline().split())
websites = {}
for _ in range(N):
    website, password = sys.stdin.readline().split()
    websites[website] = password

for _ in range(M):
    web_name = sys.stdin.readline().rstrip()
    print(websites[web_name])