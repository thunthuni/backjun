# factor : 첫 번째 숫자가 두번째 숫자의 약수이다
# multiple: 첫 번재 숫자가 두번째 숫자의 배수이다
# neither: 첫 번째 숫자가 두번째 숫자의 약수와 배수 모두 아니다

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        if B % A == 0:
            print('factor')
        elif A % B == 0:
            print('multiple')
        else:
            print('neither')
# if A % B != 0:
