import sys

num = 0
for i in range(3):
    word = sys.stdin.readline().rstrip()
    if word.isdigit():
        if i == 0:
            num = int(word) + 3
        elif i == 1:
            num = int(word) + 2
        else:
            num = int(word) + 1
        break

if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
elif num % 3 == 0 and num % 5 != 0:
    print('Fizz')
elif num % 3 != 0 and num % 5 == 0:
    print('Buzz')
else:
    print(num)


