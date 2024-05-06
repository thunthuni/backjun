dwarves = []
for _ in range(9):
    dwarves.append(int(input()))
temp = sum(dwarves) - 100

one = 0
two = 0
for i in range(9):
    for j in range(i+1, 9):
        if dwarves[i] + dwarves[j] == temp:
            one, two = dwarves[i], dwarves[j]
            break

dwarves.remove(one)
dwarves.remove(two)
dwarves.sort()
for i in dwarves:
    print(i)