dic = {'A': 2, 'B': 2, 'C': 2, 'D': 3, 'E': 3, 'F': 3, 'G': 4, 'H': 4, 'I': 4, 'J': 5, 'K': 5, 'L': 5, 'M': 6,'N': 6, 'O': 6,'P': 7, 'Q': 7, 'R': 7, 'S': 7, 'T': 8, 'U': 8, 'V': 8, 'W': 9, 'X': 9, 'Y': 9, 'Z': 9 }

alpha = input()
result = 0
for a in alpha:
    result += dic.get(a)
print(result + len(alpha))


####### 남의 코드 #######
# 딕셔너리 L[key] 를 하면 value 를 얻을 수 있다
L = {2:'ABC',3:'DEF',4:'GHI',5:'JKL',6:'MNO',7:'PQRS',8:'TUV',9:'WXYZ'}
iL = list(input())
n = 0

for i in iL:
    for j in range (2,10):
        if i in L[j]:
            n+=j+1
print(n)
