import sys

N = int(sys.stdin.readline())

for _ in range(N):
    string = sys.stdin.readline()
    tmp = 0
    signal = True
    for i in string:
        if i == '(':
            tmp += 1
        elif i == ')':
            tmp -= 1
        if tmp < 0:
            signal = False
    if tmp == 0 and signal:
        print('YES')
    else:
        print('NO')