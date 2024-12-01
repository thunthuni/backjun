import sys
N = int(sys.stdin.readline())

words = [[] for _ in range(51)]
for _ in range(N):
    word = sys.stdin.readline().strip('\n')
    if word not in words[len(word)]:
        words[len(word)].append((word))


for lst in words:
    for word in sorted(lst):
        print(word)

# new_words = sorted(words, key = lambda x:x[1])

# import sys
# input = sys.stdin.readline
# n = int(input())
#
# arr = []
# for _ in range(n):
#     arr.append(input().strip())
#
# arr = list(set(arr))
# arr.sort()
# arr.sort(key = lambda x:(len(x), ord(x[0])))
#
# print("\n".join(arr))