"""
# 퀴즈1
x = 10
y = 3

def get_quotient_remainder(a, b):
    return a // b, a % b

quotient, remainder = get_quotient_remainder(x, y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))
"""

# 퀴즈2
x, y = map(int, input().split())
def calc(a, b):
    return a + b, a - b, a * b, float(a / b)
a, s, m, d = calc(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))
