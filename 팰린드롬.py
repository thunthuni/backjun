import sys
input = sys.stdin.readline

word = input()
N = len(word)
i = 0
j = N-1
result = 0
while i < N//2 and j > N//2:
    if word[i] != word[j]:
        break
    else:
        i += 1
        j -= 1
    result = 1
print(result)
    