import sys
# input = sys.stdin.readline

N, M = map(int, input().split())  # 1

lst = set() # 1
result = []  # 1
for _ in range(N):  # N
    lst.add(input())

# N*M 500,000 * 500,000
for i in range(M):  # M
    a = input()  # 1
    if a in lst:  # 1
        result.append(a)  # 1

result.sort()
print(len(result))
print(*result, sep='\n')


