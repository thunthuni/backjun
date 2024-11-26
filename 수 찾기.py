import sys
input = sys.stdin.readline


def binarySearch(s, e, num):
    result = False
    while s < e:  # 범위가 1이 될 때까지
        m = (s + e) // 2  # 중앙값
        if num == numbers[m] or num == numbers[s] or num == numbers[e-1]: # 끝까지 안가도 찾아지면 바로 끝내기
            result = True
            break
        if num > numbers[m]:  # 찾으려는 값이 중앙값보다 크다면
            s = m + 1  # 중앙값 + 1 이 시작점
        else:  # 찾으려는 값이 중앙값보다 작다면
            e = m  # 중앙값이 끝점

    return result


N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
M = int(input())
is_num = list(map(int, input().split()))


for num in is_num:
    if binarySearch(0, N, num):
        print(1)
    else:
        print(0)