temp = input()  # 입력값
word = temp.upper()  # 모두다 대문자로 만들기
word_set = list(set(word))  # 반복 없는 문자
candidates = []
for s in word_set:
    candidates.append(word.count(s))
if candidates.count(max(candidates)) > 1:
    print('?')
else:
    idx = candidates.index(max(candidates))
    print(word_set[idx])
