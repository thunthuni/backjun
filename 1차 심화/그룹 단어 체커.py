T = int(input())
cnt = 0
for tc in range(1, T+1):
    word = list(input())
    first = word.pop(0)
    stack = [first]
    for w in word:
        if w != stack[-1]:
            stack.append(w)

    if len(stack) == len(set(stack)):
        cnt += 1
print(cnt)