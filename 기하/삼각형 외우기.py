
while True:
    lengths = []
    a, b, c = map(int, input().split())
    if a == 0 & b == 0 & c == 0:
        break
    else:
        lengths.append(a)
        lengths.append(b)
        lengths.append(c)
        lengths.sort()
        if lengths[0] + lengths[1] > lengths[-1]:
            if len(set(lengths)) == 1:
                print('Equilateral')
            elif len(set(lengths)) == 2:
                print('Isosceles')
            else:
                print('Scalene')
        else:
            print('Invalid')


