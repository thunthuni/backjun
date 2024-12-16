import sys


def GCD(x, y):
    while(y):
        x, y = y, x % y
    return x


def LCM(x, y):
    result = (x*y) // GCD(x,y)
    return result


N, M = map(int, sys.stdin.readline().split())
print(GCD(N, M))
print(LCM(N, M))