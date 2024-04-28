arr = [list(input()) for _ in range(5)]
result = ''

max_v = 0
for i in range(5):
    if max_v < len(arr[i]):
        max_v = len(arr[i])
for i in range(5):
    length = len(arr[i])
    if length < max_v:
        while length < max_v:
            arr[i].append('!')
            length = len(arr[i])
for c in range(max_v):
    for r in range(5):
        if arr[r][c] != '!':
            result += arr[r][c]
print(result)

################ 남의 코드 ######################
# 입력 받은 문자열을 저장할 리스트
lines = [input() for _ in range(5)]

# 결과를 저장할 문자열
result = ''

# 최대 길이를 구하고 각 열마다 문자를 읽어 result에 추가
max_length = max(len(line) for line in lines)
for i in range(max_length):
    for line in lines:
        if i < len(line):
            result += line[i]

# 결과 출력
print(result)

