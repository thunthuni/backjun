arr = [list(map(int,input().split())) for _ in range(9)]

max_v = []
position = []
for r in range(9):
    maxx = max(arr[r])
    max_v.append(maxx)
    position.append((r,arr[r].index(maxx)))

r_max = max(max_v)
idx = max_v.index(r_max)

print(r_max)
print(position[idx][0]+1, position[idx][1]+1)