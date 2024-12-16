# 스택에 push하는 순서는 반드시 오름차순
# 스택을 이용해 수열을 만들 수 있는지 없는지 알아내기
# 어떤 순서로 push 와 pop 연산을 수행해야 하는지
# 어떻게 풀어야 하나~
# 일단 넣어 result append( +)
# 언제까지?
# stack[-1] 이 sequnece[0] 인가요?
# 그렇다면 pop(result pop(-)) 해서 stack 에 넣고 sequence[0]도 pop!
# 그래서 이걸 언제까지 반복? num을 끝까지 다 돌때까지
# 그리고 나서 sequence랑 stack 이 일치한다면 is_possible 는 true 아니면 false
# true 면 result 출력해


import sys
from collections import deque

N = int(sys.stdin.readline())
input_sequence = []
result_sequence = []  # 비교할 결과 수열

numbers = list(range(1, N+1))  # 재료들
result = ['+']  # 연산자 넣을 리스트
is_possible = False

for num in range(N):
    input_sequence.append(int(sys.stdin.readline()))


stack = [1]  # 재료를 넣을 스택
sequence = deque(input_sequence)  # 계산할 때 사용할 수열

n_idx = 1
s_idx = 0
while stack:
    if n_idx == N and stack[-1] != sequence[0]:
        break
    if stack and stack[-1] == sequence[0]:
        result_sequence.append(stack.pop(-1))  # 비교 수열에 넣고
        sequence.popleft()  # [0] pop 하고
        result.append('-')  # 연산자 넣고
    elif not stack:
        stack.append(numbers[n_idx])
        result.append('+')
        n_idx += 1
    else:
        stack.append(numbers[n_idx])
        result.append('+')
        n_idx += 1

if input_sequence == result_sequence:
    print(*result, sep='\n')
else:
    print('NO')


