
def hello():
    print('Hello, world!')

hello()

def add(a, b):
    print(a + b)

add(10, 20)

def add_re(a, b):
    """이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수"""
    return a + b

x = add_re(10, 20)
print(x)

# 함수의 docstring 출력
print(add_re.__doc__)

# help 객체
help(add_re)

# return값 여러개일때
def add_sub(a, b):
    return a + b, a - b

x, y = add_sub(10, 20)
print(x)
print(y)

z = add_sub(10, 20)
print(z)
