"""
# 1. lambda 사용전 함수
def plus_ten(x):
    return x + 10

print(plus_ten(1))
"""
"""
# lambda expression으로 작성
lambda x: x + 10
"""
"""
# lambda expreesion을 변수에 할당
plus_ten = lambda x: x + 10
print(plus_ten(1))
"""
"""
# 람다표현식 자체를 호출
(lambda x: x + 10)(1)
print((lambda x: x + 10)(1))
"""
"""
# 람다표현식 변수 사용x
(lambda x: y = 10; x + y)(1)
print((lambda x: y = 10; x + y)(1))
"""
"""
# 람다 밖에 있는 변수 사용
y = 10
(lambda x: x + y)(1)
print((lambda x: x + y)(1))
"""
"""
# 람다 표현식 인수로 사용-1
def plus_ten(x):
    return x + 10

list(map(plus_ten, [1, 2, 3]))

print(list(map(plus_ten, [1, 2, 3])))
"""
"""
# 람다 표현식 인수로 사용-2
list(map(lambda x: x + 10, [1, 2, 3]))

print(list(map(lambda x: x + 10, [1, 2, 3])))
"""
"""
# lambda 매개변수 없는 함수 만들기
(lambda : 1)()
print((lambda : 1)())

x = 10
(lambda : x)()
print((lambda : x)())
"""
"""
# 람다와 if
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p = list(map(lambda x: str(x) if x % 3 == 0 else x, a))

print(p)
"""
"""
# 람다와 if-2
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p = list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))

print(p)
"""
"""
# 람다와 if-2 알아보기 쉽게 def 로
def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x + 10

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p = list(map(f, a))

print(p)
"""
"""
# map에 객체 여려개 넣기
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
p = list(map(lambda x, y: x * y, a, b))

print(p)
"""
"""
# filter-1
def f(x):
    return x > 5 and x < 10

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
p = list(filter(f, a))

print(p)
"""
"""
# filter-2
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
p = list(filter(lambda x: x > 5 and x < 10, a))

print(p)
"""
"""
# reduce-1
def f(x, y):
    return x + y

a = [1, 2, 3, 4, 5]
from functools import reduce
p = reduce(f, a)

print(p)
"""
"""
# reduce-2
a = [1, 2, 3, 4, 5]
from functools import reduce
p = reduce(lambda x, y: x + y, a)

print(p)
"""
"""
# list comprehension
# list(filter(lambda x: x > 5 and x < 10, a)) 보다 간단
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
p = [i for i in a if i > 5 and i < 10]

print(p)
"""
"""
# reduce 대신
# for, while loop 사용
a = [1, 2, 3, 4, 5]
x = a[0]
for i in range(len(a) - 1):
    x = x + a[i + 1]

print(x)
"""
"""
# 퀴즈1
files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']

print(list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, files)))

print(list(filter(lambda x: '.jpg' in x or '.png' in x, files)))
"""

# 퀴즈2
files = input().split()
print(list(map(lambda x: x.zfill(len(x)) if x.find('.') >= 3 else x.zfill(len(x)+(3 - x.find('.'))), files)))
print(list(map(lambda x: '{0:03d}'.format(int(x.split('.')[0])) + '.' + (x.split('.')[1]), files)))