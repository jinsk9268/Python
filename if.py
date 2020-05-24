"""x = int(input())

if x == 10:
    print('10 입니다')

if x == 20:
    print('20 입니다')"""

"""x = 5

if x != 10:
    print('ok')"""

"""x = int(input())
y = input()
if y == 'Cash3000':
    print(x-3000)
if y == 'Cash5000':
    print(x-5000)"""

"""price = int(input('가격을 입력하게요 : '))
coupon = input('쿠폰을 입력하세요 : ')
if coupon == 'Cash3000':
    price -= 3000
if coupon == 'Cash5000':
    price -= 5000
print(price)"""

"""x = 5

if x == 10:
    print('10입니다')
else:
    print('10이 아닙니다')
    print('무엇일까요?')"""

"""# True는 참
if True:
    print('참') # 참 실행
else:
    print('거짓')

# False는 거짓
if False:
    print('참')
else:
    print('거짓') # 거짓 실행

# None은 거짓 (실제 코드작성할때 변수에 들어있는 값, 함수 결과가 None인 경우가 많으므로 주의
if None:
    print('참')
else:
    print('거짓') # 거짓 실행

# 숫자는 정수(2진수, 10진수 16진수),실수 와 관계없이 0이면 거짓, 0이 아닌수는 참
# 0은 거짓   
if 0:
    print('참')
else:
    print('거짓') # 거짓 실행

# 1은 참
if 1:
    print('참') # 참 실행
else:
    print('거짓')

# 문자열 (문자열은 내용이 있을때 참, 빈 문자열은 거짓)
# 문자열이 있을때
if 'hello':
    print('참') # 참 실행
else:
    print('거짓')

# 문자열이 없을때
if '':
    print('참')
else:
    print('거짓') # 거짓 실행"""

"""x = 10
y = 20

if x == 10 and y == 20:
    print('참')
else:
    print('거짓')"""

"""written_test = 75
coding_test = True

if written_test >= 80 and coding_test==True:
    print('합격')
else:
    print('불합격')"""
"""
kor = int(input())
eng = int(input())
mat = int(input())
sci = int(input())
"""

"""kor, eng, mat, sci = map(int, input().split())
avg = (kor+eng+mat+sci)/4
if kor < 0 or kor > 100 or eng < 0 or eng > 100 or mat < 0 or mat > 100 or sci < 0 or sci > 100:
    print('잘못된 점수')
else:
    if avg >= 80:
        print('합격')
    else:
        print('불합격')"""

"""button = int(input())

if button == 1:
    print('콜라')
elif button == 2:
    print('사이다')
elif button == 3:
    print('환타')
else:
    print('제공하지 않는 메뉴')"""

x = int(input())

if 11 <= x <= 20:
    print('11~20')
elif 21 <= x <= 30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')
    

  
    
