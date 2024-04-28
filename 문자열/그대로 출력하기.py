import sys
sys.stdin = open('문자열/input.txt')

while True:
    try:
        sentence = input().strip()
        print(sentence)
    except:
        break
