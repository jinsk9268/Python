"""
# 재귀호출 recursive call, maximum recursion depth 초과, RecursionError 발생
def hello():
    print('Hello, world')
    hello()

hello()
"""
"""
# 재귀호출 종료 조건 만들기
def hello(count):
    if count == 0:
        return
    print('Hello, world!', count)

    count -= 1
    hello(count)

hello(5)
"""
"""
# 팩토리얼 구현
# n이 1일때
# 1을 반환하고 recursive 호출을 끝냄
# n과 factorial 함수에 n-1을 넣어서 반환된 값을 곱함
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n -1)

print(factorial(5))
"""
"""
# recursive call로 palindrome 판별하기
def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

print(is_palindrome('hello'))
print(is_palindrome('level'))
"""

# 재귀호출로 피보나치 함수
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    #if n == 2:
        #return 1
    return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))