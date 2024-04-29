dwarves = []
for _ in range(9):
    dwarves.append(int(input()))
temp = sum(dwarves) - 100
fake = []
dwarves.sort()
for i in range(9):
    for j in range(i+1, 9):
        if dwarves[i] + dwarves[j] == temp:
            fake.append(dwarves[i])
            fake.append(dwarves[j])
for i in dwarves:
    if i not in fake:
        print(i)
