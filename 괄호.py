import sys

N = int(sys.stdin.readline())

for _ in range(N):
    stack = []
    ps = input()
    flag = True
    for i in ps:
        if not stack:
            if i == '(':
                stack.append(i)
            else:
                print('NO')
                flag = False
                break
        else:
            if i == '(':
                if stack[-1] == '(':
                    stack.append(i)
                else:
                    stack.pop(-1)
            else:
                if stack[-1] == ')':
                    stack.append(i)
                else:
                    stack.pop(-1)
    if stack and flag:
        result = 'NO'
        print(result)
    elif not stack and flag:
        print('YES')
