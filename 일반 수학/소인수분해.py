# import sys
# sys.stdin = open('input.txt')

N = int(input())
lst = []
i = 2

while N > 1: 
    if N % i == 0:
        N = N / i 
        lst.append(i)
        i = 2
    else: 
        i += 1

if len(lst) >= 1:
    for i in sorted(lst):
        print(i)

