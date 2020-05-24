"""
# iterator
class Counter:
    def __init__(self, stop):
        # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.current = 0
        # 반복을 끝낼 숫자
        self.stop = stop

    def __iter__(self):
        # 현재 인스턴스를 반환
        return self

    def __next__(self):
        # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
        if self.current < self.stop:
            # 반환할 숫자를 변수에 저장
            r = self.current
            # 현재 숫자를 1 증가시킴
            self.current += 1
            # 숫자를 반환
            return r
        # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을때
        else:
            # 예외 발생
            raise StopIteration

for i in Counter(3):
    print(i, end = ' ')
"""
"""
# index iterator
class Counter:
    def __init__(self, stop):
        # 반복을 끝낼 숫자
        self.stop = stop

    # 인덱스를 받음
    def __getitem__(self, index):
        # 인덱스가 반복을 끝낼 숫자보다 작을 때
        if index < self.stop:
            # 인덱스를 반환
            return index
        # 인덱스가 반복을 끝낼 숫자보다 크거가 같을때
        else:
            # 예외 발생
            raise IndexError

print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

for i in Counter(3):
    print(i, end=' ')
"""
"""
# iter function
import random

while True:
    i = random.randint(0, 5)
    if i == 2:
        break
    print(i, end = ' ')
"""
"""
# quiz-1
class MultipleIterator:
    def __init__(self, stop, multiple):
        self.stop = stop
        self.multiple = multiple
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current * self.multiple < self.stop:
            return self.current *  self.multiple
        else:
            raise StopIteration

for i in MultipleIterator(20, 3):
    print(i, end = ' ')

print()
for i in MultipleIterator(30, 5):
    print(i, end = ' ')
"""
"""
# quiz-2
class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __getitem__(self, index):
        if index < self.stop - self.start:
            h = (self.start + index)//60//60%24
            m = (self.start + index)//60%60
            s = (self.start + index)%60
            return '{0:02d}:{1:02d}:{2:02d}'.format(h, m, s)
        else:
            raise IndexError

start, stop, index = map(int, input().split())

for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')
"""
"""
# yield
def number_generator():
    yield 0
    yield 1
    yield 2

for i in number_generator():
    print(i)

g = number_generator()
print(g)
print(dir(g))
"""
"""
# yield 동작과정
def number_generator():
    yield 0 # 0을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
    yield 1 # 1을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
    yield 2 # 2을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보

g = number_generator()

# yield를 사용하여 함수 바깥으로 전달한 값은 next의 반환값으로 나옴
a = next(g)
print(a)

b = next(g)
print(b)

c = next(g)
print(c)
"""
"""
# generator return
def one_generator():
    yield 1
    return 'return에 지정한 값'

try:
    g = one_generator()
    next(g)
    next(g)
except StopIteration as e:
    print(e)
"""
"""
# creat generator
def number_generator(stop):
    n = 0   # 0부터 시작
    while n < stop: # 현재 숫자가 반복을 끝낼 숫자보다 작을때까지 반복
        yield n # 현재 숫자를 외부로 전달
        n += 1  # 현재 숫자를 증가시킴

for i in number_generator(3):
    print(i)

print()

g = number_generator(3)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
"""
"""
# yield function call
def upper_generator(x):
    for i in x:
        yield i.upper() # 함수의 반환값을 바같으로 전달

fruits = ['apple', 'pear', 'grape', 'pineapple', 'orange']
for i in upper_generator(fruits):
    print(i)
"""
"""
# yield from
def number_generator():
    x = [1, 2, 3]
    yield from x    # list에 들어있는 요소를 한 개씩 외부로 전달

for i in number_generator():
    print(i)

g = number_generator()
print(next(g))
print(next(g))
print(next(g))
print(next(g))  # 오류 발생
"""
"""
# generator yield from
def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1

def three_generator():
    yield from number_generator(3)  # 숫자를 3번 바깥으로 전달

for i in three_generator():
    print(i)
"""
"""
# quiz 1
def file_read():
    with open('words4.txt') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            yield line.strip('\n')

for i in file_read():
    print(i)
"""

# 퀴즈2
def prime_number_generator(start, stop):
    for n in range(start, stop+1):
        is_prime = True
        for i in range(2,n):
            if n % i == 0:
                is_prime = False
        if is_prime == True:
            yield n

start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')
