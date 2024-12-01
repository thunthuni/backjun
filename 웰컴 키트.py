import sys

# 웰컴키트: 티셔츠 1 장 + 펜 1 자루
# 키트 제작 주문 방법
    # 티셔츠는 같은 사이즈의 T장 묶음
    # 펜은 (P자루씩 묶음) or (한 자루씩)
# 티셔츠는 남아도 괜춘 but 펜은 정확히

# 구해야 하는 것: 티셔츠를 T장씩 최소 몇 묶음 , 펜을 P자루씩 최대 몇 묶음 & 펜을 한 자루씩 몇 개
N = int(sys.stdin.readline())
sizes = list(map(int, sys.stdin.readline().split()))
T, P = map(int, sys.stdin.readline().split())

shirts = 0
pens = 0
pen = 0
for i in range(6):
    shirts += sizes[i] // T
    if sizes[i] % T > 0:
        shirts += 1
pens += N // P
pen += N % P

print(shirts)
print(pens, pen)
