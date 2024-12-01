# 한거번에 생각하려고 하지 말자
# 지금 내가 헷갈려 하는 것은 8*8 을 어떻게 다 확인할 것인가 
# 먼저 c 0-8 까지 갔다가 
# r은 그대로 c +1 해서

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

min = 1
num = 0 
r = 0
c = 0 

for r in range(N-7):
    for c in range(M-7):
        for i in range(r, r+8):
            for j in range(c, c+7):
                if arr[i][j] == arr[i][j+1]:
                    arr[i][j+1] = 1
                    num += 1
        if num < min:
            min = num
    
        
print(min)