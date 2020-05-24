"""
word = input('단어를 입력하세요: ')

# 회문 판별값을 저장할 변수, 초기화 True
is_palindrome = True

# 0부터 문자열 길이의 절반 만큼 반복
for i in range(len(word) // 2):
    if word[i] != word[-1 - i]:     # 왼쪽 문자와 오르녺 문자를 비교하여 문자가 다르면
        is_palindrome = False       # 회문이 아님
        breakpoint      #반복문 탈출

print(is_palindrome)    # 회문 판별값 출력
"""
"""
# 시퀀스 뒤집기로 검사
word = input('단어를 입력하세요: ')

# 원래 문자열과 반대로 뒤집은 문자열을 비교
# word[::-1]은 문자열 전체에서 인덱스를 1씩 감소시키면서 요소가져옴, 역순으로 출력
print(word == word[::-1])
"""
"""
# reversed 사용하기
word = 'level'
print(list(word) == list(reversed(word)))
print(list(word))
print(list(reversed(word)))
"""
"""
# join과 reversed 사용하기
word = 'level'
print(word == ''.join(reversed(word)))
print(word)
print(''.join(reversed(word)))
"""
"""
# 2-gram 출력하기 loop로
text = 'Hello'

# 2-gram이므로 문자열의 끝에서 한글자 앞까지만 반복해야하기 때문에 -1
for i in range(len(text) -1):
    print(text[i], text[i + 1], sep = '')
    # 현재 문자와 그다음 문자 출력
"""
"""
# 문자열 출력
# 공백을 기준으로 문자열을 분리하여 리스트로 만듦
text = 'this is python script'
words = text.split()

# 2-gram 이므로 리스트의 마지막에서 element 한 개 앞까지만 반복
# 현재 문자열과 그 다음 문자열 출력
for i in range(len(words) - 1):
    print(words[i], words[i + 1])
"""
"""
# zip으로 2-gram 만들기
text = 'hello'

# zip으로 text와 text[1:]의 각 요소를 묶어서 튜플로 만듬
two_gram = zip(text, text[1:])
for i in two_gram:
    print(i[0], i [1], sep = '')
"""
"""
# zip과 표현식
text = 'hello'
a = list(zip(*[text[i:] for i in range(3)]))
print(a)
"""
"""
# 퀴즈
n = int(input())
text = input()
words = text.split()

if len(words) < n:
    print('worng')
else:
    n_gram = zip(*[words[i:] for i in range(n)])
    for i in n_gram:
        print(i)
"""
"""
# 퀴즈
with open('words3.txt', 'r') as file:
    word = file.readlines()
    pal = [ i.strip('\n') for i in word]
    for i in pal:
        if i == i[::-1]:
            print(i)
"""
with open('words3.txt', 'r') as file:
    word = file.readlines()
    word = [ i.strip('\n') for i in word]
    for i in word:
        if i == i[::-1]:
            print(i)

