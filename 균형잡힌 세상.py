import sys

flag = True

while flag:
    string = sys.stdin.readline()
    if string == '.\n':
        flag = False
        break
    stack = []
    signal = True

    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop(-1)
            else:
                signal = False
        elif i == '[':
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop(-1)
            else:
                signal = False

    if not stack and signal:
        print('yes')
    else:
        print('no')

