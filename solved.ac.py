# 아무 의견이 없다면 문제의 난이도 = 0
# 의견이 하나 이상 있다면 의견의 30% 절사평균
# 30% 절사평균: 위에서 15퍼 (반올림), 아래에서 15퍼 (반올림) 제외한 평균
# 계산된 평균도 반올림

import sys
import math


def myRound(n):
    return math.floor(n + 0.5)


N = int(sys.stdin.readline())
minus = myRound(N * 0.15)
level_cnt = [0] * 31
result = -1
if N == 0:
    result = 0

else:
    for _ in range(N):
        level_cnt[int(sys.stdin.readline())] += 1

    tmp = minus
    for i in range(1, 31):
        if tmp <= 0:
            break
        else:
            level = level_cnt[i]
            if level:
                if level <= tmp:
                    tmp -= level
                    level_cnt[i] = 0
                else:
                    level_cnt[i] -= tmp
                    tmp = 0

    tmp2 = minus
    for i in range(30, 0, -1):
        if tmp2 <= 0:
            break
        else:
            level = level_cnt[i]
            if level:
                if level <= tmp2:
                    tmp2 -= level
                    level_cnt[i] = 0
                else:
                    level_cnt[i] -= tmp2
                    tmp2 = 0

if result == 0:
    print(0)
else:
    sum_v = 0
    for i in range(1, 31):
        if level_cnt[i]:
            sum_v += level_cnt[i] * i
    print(myRound(sum_v / (N-minus*2)))
# print(level_cnt)

