import sys
input = sys.stdin.readline

word = list(input().strip())
N = len(word)
reversed_word = reversed(word)
if word == reversed_word:
    print(1)
else:
    print(0)
print(list(reversed_word))
print(word)
print(word==reversed_word)