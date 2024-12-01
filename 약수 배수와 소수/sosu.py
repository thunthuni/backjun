N = int(input())
M = int(input())
lst = []
for num in range(N, M+1):
    a = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                a += 1
                break

        if a == 0:
            lst.append(num)
if len(lst) > 0:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)
