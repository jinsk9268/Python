"""
# global_variable
x = 10      # global variable
def foo():
    print(x)    # global variable 출력

foo()
print(x)    # global variable 출력
"""
"""
# local variable
def foo():
    x = 10      # foo의 지역 변수
    print(x)    # foo의 지역 변수 출력

foo()
print(x)    # 에러 발생, foo의 지역 변수는 출력할 수 없다
"""
"""
# 전역변수, 지역변수 범위보기
x = 10      # global variable
def foo():
    x = 20  # x는 foo의 local variable
    print(x)    # foo의 local variable 출력

foo()
print(x)    # global variable 출력
"""
"""
# 함수안에서 전역변수 값 변경
x = 10      # global variable
def foo():
    global x    # global variable x를 사용하겠다고 설정
    x = 20      # x는 global variable
    print(x)    # global variable 출력

foo()
print(x)    # global variable 출력
"""
"""
# 함수 안에서 전역변수 생성
# global variable 가 없는 상태
def foo():
    global x    # x를 global variable 로 만듦
    x = 20      # global variable x에 값 할당
    print(x)    # global variable 출력

foo()
print(x)    # global variable 출력
"""
"""
# namespace
x = 10
print(locals())

def foo():
    x = 10
    print(locals())

foo()
"""
"""
# nested function
def print_hello():
    hello = 'Hello, world'
    def print_message():
        print(hello)
    print_message()

print_hello()
"""
"""
# fuction local error
def A():
    x = 10  # A의 지역 변수 x
    def B():
        x = 20  # x에 20 할당, B의 지역변수 x
    B()
    print(x)    # A의 지역 변수 x 출력

A()
"""
"""
# nonlocal 키워드 사용
def A():
    x = 10  # A의 지역 변수 x
    def B():
        nonlocal x  # 현재 함수의 바깥쪽에 있는 지역 변수 사용
        x = 20  # A의 지역 변수 x에 20 할당
    B()
    print(x)    # A의 지역변수 x 출력

A()
"""
"""
# nonlocal 변수 찾는 순서
def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()

A()
"""
"""
# global로 전역변수 사용
x = 1
def A():
    x = 10
    def B():
        x = 20
        def C():
            global x
            x = x + 30  # global variable x 사용 (1)
            print(x)
        C()
    B()

A()
"""
"""
# closure
def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b    # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
    return mul_add  # mul_add 함수를 반환

c = calc()

print(c(1), c(2), c(3), c(4), c(5))
"""
"""
# lambda로 클로저 만들기
def calc():
    a = 3
    b = 5
    return lambda x: a * x + b  # 람다 표현식을 반환

c = calc()
print(c(1), c(2), c(3), c(4), c(5))
"""
"""
# 클로저 nonlocal
def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a * x + b   # a*x+b의 결과 함수 calc의 지역변수 total에 누적
        print(total)
    return mul_add

c = calc()
c(1)
c(2)
c(3)
"""
"""
# 퀴즈1
def counter():
    i = 0
    def count():
        nonlocal i
        i += 1
        return i
    return count    # 함수를 리턴할때는 () 붙이면 안됨

c = counter()
for i in range(10):
    print(c(), end = ' ')
"""

# 퀴즈2
def countdown(n):
    i = n + 1
    def count():
        nonlocal i
        i -= 1
        return i
    return count

n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end = ' ')