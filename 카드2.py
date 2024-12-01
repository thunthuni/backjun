
# N 장의 카드 차례로 1~N 번호의 카드
# 내림차순으로 카드가 놓여있음
# 카드가 한장이 남게 되는 과정:
    # 맨 위의 카드 버림
    # 버린 후에 젤 위에 있는 카드 맨 밑으로
    # 반보쿠
# 마지막에 남는 카드는?

import sys

N = int(sys.stdin.readline())

stack = set()
for i in range(1, N+1):   # O(N)
    stack.add(i)

while len(stack) >= 1:
    if len(stack) == 1:
        print(*stack)
        break

    else:
        stack.pop()
        stack.add(stack.pop())

# print(stack)
## 이 문제에서 사용하는 연산 정리 해봐 예를들어 맨 뒤추가 맨 앞 추가 이런식으로
# 그리고 너가 아는 자료구조들을 하나하나 다 생각해봐
# 힌트 -> 규칙 안 찾아도 됨


