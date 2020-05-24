"""
# exception
def ten_dev(x):
    return 10 / x

print(ten_dev(2))

print(ten_dev(0))
"""
"""
# try exception
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
    print(y)

# 예외가 발생했을 때 실행됨
except:
    print('예외가 발생했습니다.')
"""
"""
# try exception - 2
y = [10, 20, 30]

try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)

# 숫자를 0으로 나눠서 에러가 발생했을 때 실행
except ZeroDivisionError:
    print('숫자를 0으로 나눌 수 없습니다.')

# 범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행됨
except IndexError:
    print('잘못된 인덱스입니다.')
"""
"""
# try except as
y = [10, 20, 30]

try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
except ZeroDivisionError as e:
    print('숫자를 0으로 나눌 수 없습니다.', e)
except IndexError as e:
    print('잘못된 인덱스입니다.', e)
# 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
except Exception as e:
	print('예외가 발생했습니다.', e)
	
# as 뒤에 변수를 지정하면서 에러를 받아옴
# e에 저장된 에러 메시지 출력	
"""
"""
# try except else
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 /x
except ZeroDivisionError:
    print('숫자를 0으로 나눌 수 없습니다.')
else:
    print(y)

# 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
# try의 코드에서 예외가 발생하지 않았을 때 실행됨
"""
"""
# try except finally
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:
    print('숫자를 0으로 나눌 수 없습니다.')
else:
    print(y)
finally:
    print('코드 실행이 끝났습니다.')

# 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
# try의 코드에서 예외가 발생하지 않았을 때 실행됨
# 예외 발생 여부와 상관없이 항상 실행 됨
"""
"""
# raise
try:
    x = int(input('3의 배수를 입력하세요: '))
    # x가 3의 배수가 아니라면
    if x % 3 != 0:
        # 예외를 발생시킴
        raise Exception('3의 배수가 아닙니다.')
    print(x)
# 예외가 발생했을 때 실행
except Exception as e:
    print('예외가 발생했습니다.', e)
"""
"""
# raise without try except
def three_multiple():
    x = int(input('3의 배수를 입력하세요: '))
    # x가 3의 배수가 아니면
    if x % 3 != 0:
        # 예외를 발생시킴
        raise Exception('3의 배수가 아닙니다.')
    print(x)
# 현재 함수안에는 except가 없으므로 , 예외를 상위 코드 블록으로 넘김

try:
    three_multiple()
#하위 코드 블록에서 예외가 발생해도 실행됨
except Exception as e:
    print('예외가 발생했습니다.', e)

# 하위토드에서도 예외처리 없을때 에러발생
# three_multiple()
"""
"""
# re-raise
def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        # x가 3의 배수가 아니면
        if x % 3 != 0:
            # 예외를 발생시킴
            raise Exception('3의 배수가 아닙니다.')
        print(x)
    # 함수 안에서 예외를 처리함
    except Exception as e:
        print('three_multiple 함수에서 예외가 발생했습니다.', e)
        # raise로 현재 예외를 다시 발생시켜서 상위 코드 블록으로 넘김
        raise

try:
    three_multiple()
# 하위 코드 블록에서 예외가 발생해도 실행
except Exception as e:
    print('스크립트 파일에서 예외가 발생')
"""
"""
# re-raise 2
def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        # x가 3의 배수가 아니면
        if x % 3 != 0:
            # 예외를 발생시킴
            raise Exception('3의 배수가 아닙니다.')
        print(x)
    # 함수 안에서 예외를 처리함
    except Exception as e:
        print('three_multiple 함수에서 예외가 발생했습니다.', e)
        # raise로 현재 예외를 다시 발생시켜서 상위 코드 블록으로 넘김
        raise RuntimeError('three_multiple 함수에서 예외가 발생했습니다.')

try:
    three_multiple()
# 하위 코드 블록에서 예외가 발생해도 실행
except Exception as e:
    print('스크립트 파일에서 예외가 발생')
"""
"""
# assert
x = int(input('3의 배수를 입력하세요: '))
# 3의 배수가 아니면 예외 발생, 3의 배수이면 그냥 넘어감
assert x % 3 == 0, '3의 배수가 아닙니다.'
print(x)
"""
"""
# exception class
# Exception을 상속받아서 새로운 예외를 만듦
class NotThreeMultipleError(Exception):
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')

def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        # x가 3의 배수가 아니면
        if x % 3 != 0:
            # NotThreeMultipleError 예외를 발생시킴
            raise NotThreeMultipleError
        print(x)
    except Exception as e:
        print('예외가 발생했습니다.', e)

three_multiple()
"""
"""
# exception class-2
# Exception만 상속받고
class NotThreeMultipleError(Exception):
    # 아무것도 구현하지 않음
    pass

def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        # x가 3의 배수가 아니면
        if x % 3 != 0:
            # 예외를 발생시킬 때 에러 메시지늘 넣음
            raise NotThreeMultipleError('3의 배수가 아닙니다.')
        print(x)
    except Exception as e:
        print('예외가 발생했습니다.', e)

three_multiple()
"""
"""
# 퀴즈1
try:
    file = open('maria.txt', 'r')
except FileNotFoundError:
    print('파일이 없습니다.')
else:
    s = file.read()
    file.close()
"""

# 퀴즈2-1
class NotPalindromeError(Exception):
    pass

def palindrome(word):
    if word != word[::-1]:
        raise NotPalindromeError('회문이 아닙니다')
    print(word)

try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)

# 퀴즈2-2
class NotPalindromeError(Exception):
    def __init__(self):
        super().__init__('회문이 아닙니다.')

def palindrome(word):
    if word != word[::-1]:
        raise NotPalindromeError
    print(word)

try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)



