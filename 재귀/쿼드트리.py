
def recur(r, c, n):   # row, col, n
    global arr
    global result

    temp = arr[r][c]
    for row in range(r, r+n):
        for col in range(c, c+n):
            if arr[row][col] != temp:
                n = n // 2
                result += "("
                left_top = recur(r, c, n)
                right_top = recur(r, c + n, n)
                left_down = recur(r + n, c, n)
                right_down = recur(r + n, c + n, n)
                result += ")"
                return f"({left_top}{right_top}{left_down}{right_down})"

    result += temp


N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
result = ""
recur(0,0, N)
print(result)



# 어디서 막혔을까요?
# 작은 사각형부터? 큰 사각형 부터? => 큰 것 부터 하는게 더 효율적일 것 같다
# 그럼 가장 큰 사각형이 1, 0 둘 중 하나로만 이루어져있는지 체크
    # 하나하나 다 돌기보다 set 을 이용해서 체크하자

# 그 다음 생각해봐야 할 것
# 만약 가장 큰 사각형이 하나로만 이루어진게 아니라면?
# 왼위 -> 오위 -> 왼아 -> 오아 방향으로 (N/2 * N/2) 사각형을 체크 해봐야 하는데
#


# 재귀함수로 뭐할거야?
    # 1. 사각형이 하나로만 이루어졌는지 확인 하는 코드
        # 2. 맞다면 그 하나로만 이루어진 숫자를 출력하기
            # 3. 다음 체크해야 하는 사각형으로 이동할 수 있는 업데이트 된 r, c, n 을 가지고 함수를 다시 호출
        # 4. 아니라면 다시 사각형을 나누기
            # 1. 사각형이 하나로만 이루어졌는지 확인 하는 코드
                # 2. 맞다면 그 하나로만 이루어진 숫자를 출력하기
                    # 3. 다음 체크해야 하는 사각형으로 이동할 수 있는 업데이트 된 r, c, n 을 가지고 함수를 다시 호출
                # 4. 아니라면 다시 사각형을 나누기

    # 마지막. 종료조건은 뭐로 할거야?
        # 마지막 단위가 1 일때



# lst = []  # 값들 넣는 리스트
# for row in range(r, r+n):  # 지금 현재 n == N/2
#     for col in range(c, c+n):
#         lst.append(arr[row][col])
# if len(set(lst)) == 1:
#     print(lst[0])
# else:
#     result.extend(lst)
#     n = n/2
#     recur( n)


# if n == 1:
#     for row in range(r, r + n):  # 지금 현재 n == N/2
#         for col in range(c, c + n):
#             result.append(arr[row][col])
#     print(result)

# # temp = 0
# # for i in range(N):
# #     if len(set(arr[i])) == 1:
# #         temp += 1
# # if temp == N:
# #     result.append(str(arr[0][0]))
#
# else:
#     N = N/2


# 2. 맞다면 그 하나로만 이루어진 숫자를 출력하기
# if temp == N:
#     result.append(str(arr[r][c]))
#     # 3. 다음 체크해야 하는 사각형으로 이동할 수 있는 업데이트 된 r, c, n 을 가지고 함수를 다시 호출
#     print(result)
#     # recur(r, c+n, n)
#
# # 4. 아니라면 다시 사각형을 나누기
# else:
#     n = n/2
#     recur(r, c, n)
#     recur(r, c+n, n)
#     recur(r+n, c, n)
#     recur(r+n, c+n, n)