total_g = 0
levels = {'A+': 4.5, 'A0' : 4.0, 'B+': 3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
size_sum = 0
for _ in range(20):
    name, size, level = input().split()
    if level != 'P':
        total_g += float(size)*float(levels.get(level))
        size_sum += float(size)

print(total_g/size_sum)