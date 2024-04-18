arr = [list(input()) for _ in range(5)]
result = ''

for i in range(5):
    N = len(arr[i])
    for c in range(N):
        for r in range(5):
            result += arr[r][c]
    print(result)