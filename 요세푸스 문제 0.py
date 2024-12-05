import sys

N, K = map(int, sys.stdin.readline().split())

circle = list(range(1, N+1))
result = []
kth_cnt = 0
i = 0
while sum(circle) != 0:
    if kth_cnt != K-1:
        if circle[i] != 0:
            kth_cnt += 1
        i += 1
    else:
        if circle[i] == 0:
            i += 1
        else:
            result.append(circle[i])
            kth_cnt = 0
            circle[i] = 0
            for _ in range(i+1):
                circle.append(circle.pop(0))
            i = 0

print(result)


    # if circle[0] == 0:
    #     circle.append(circle.pop(0))
    # if kth_cnt != K-1:
    #     if circle[0] != 0:
    #         kth_cnt += 1
    #     circle.append(circle.pop(0))
    #
    # else:
    #     result.append(circle.pop(0))
    #     circle.append(0)
    #     kth_cnt = 0



print(f"<{', '.join(map(str, result))}>")

