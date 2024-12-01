dic = {10:'A',  11:'B',  12:'C',  13:'D',  14:'E',  15:'F', 16:'G',  17:'H',  18:'I', 19:'J',
        20:'K',  21:'L',  22:'M',  23:'N',  24:'O',  25:'P', 26:'Q' , 27:'R',  28:'S',  29:'T',
       30: 'U',  31:'V',  32:'W',  33:'X',  34:'Y',  35:'Z'}

N, B = list(map(int, input().split()))

lst = []
while N > 0:
    lst.append(N % B)
    N = N//B

lst.reverse()
result = ''

for i in lst:
    if i >= 10:
        result += str(dic.get(i))
    else:
        result += str(i)

print(result)