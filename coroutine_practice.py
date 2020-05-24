"""
# coroutine
def number_coroutine():
    # 코루틴을 계속 유지하기 위해 무한 루프 사용
    while True:
        # 코루틴 바깥에서 값을 받아옴, yield를 괄호로 묶어야 함
        x = (yield)
        print(x)

co = number_coroutine()
# 코루틴 안의 yield까지 코드 실행(최초 실행)
next(co)

co.send(1)  # 코루틴에 숫자 1을 보냄
co.send(2)  # 코루틴에 숫자 2를 보냄
co.send(3)  # 코루틴에 숫자 3을 보냄
"""
"""
# coroutine - 2
def sum_coroutine():
    total = 0
    while True:
        # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        x = (yield total)
        total += x

co = sum_coroutine()
print(next(co)) # 0: 코루틴안의 yield까지 코드를 실행하고 코루틴에서 나온 값 출력

print(co.send(1))   # 1: 코루틴에 숫자 1을 보내고 코루틴에서 나온 값 출력
print(co.send(2))   # 3: 코루틴에 숫자 2를 보내고 코루틴에서 나온 값 출력
print(co.send(3))   # 6: 코루틴에 숫자 3을 보내고 코루틴에서 나온 값 출력
"""
"""
# coroutine close
def number_coroutine():
    while True:
        x = (yield)
        print(x, end = ' ')

co = number_coroutine()
next(co)

for i in range(20):
    co.send(i)

co.close()  # 코루틴 종료
"""
"""
# coroutine generator exit
def number_coroutine():
    try:
        while True:
            x = (yield)
            print(x, end=' ')
    # 코루틴이 종료 될 때 GeneratorExit 예외 발생
    # close 메서드로 코루틴을 종료할 때 원하는 코드를 실행할 수 있음
    except GeneratorExit:
        print()
        print('코루틴 종료')

co = number_coroutine()
next(co)

for i in range(20):
    co.send(i)

co.close()
"""
"""
# coroutine throw
def sum_coroutine():
    try:
        total = 0
        while True:
            x = (yield)
            total += x
    except RuntimeError as e:
        print(e)
        yield total # 코루틴 바깥으로 값 전달

co = sum_coroutine()
next(co)

for i in range(20):
    co.send(i)

print(co.throw(RuntimeError, '예외로 코루틴 끝내기'))
# 190
# 코루틴의 except에서 yield로 전달받은 값
"""
"""
# yield from coroutine
def accumulate():
    total = 0
    while True:
        x = (yield) # 코루틴 바깥에서 값을 받아옴
        if x is None:   # 받아온 값이 None라면
            return total    # 합계 total을 반환
        total += x

def sum_coroutine():
    while True:
        total = yield from accumulate() # accumulate의 반환값을 가져옴
        print(total)

co = sum_coroutine()
next(co)

for i in range(1, 11):  # 1부터 10까지 반복
    co.send(i)  # 코루틴 accumulate에 숫자를 보냄
co.send(None)   # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄

for i in range(1, 101): # 1부터 100까지 반복
    co.send(i)  # 코루틴 accumulate에 숫자를 보냄
co.send(None)   # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄
"""
"""
# coroutine stopiteration
def accumulate():
    total = 0
    while True:
        x = (yield) # 코루틴 바깥에서 값을 받아옴
        if x is None:   # 받아온 값이 None이면
            return total    # StopIteration에 반환할 값을 지정 (파이썬 3.6이하)
                            # 파이썬 3.7 이상 return 값 으로
        total += x

def sum_coroutine():
    while True:
        total = yield from accumulate() # accumulate의 반환값을 가져옴
        print(total)

co = sum_coroutine()
next(co)

for i in range(1, 11):  # 1 부터 10까지 반복
    co.send(i)  # 코루틴 accumulate에 숫자를 보냄
co.send(None)   # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄

for i in range(1, 101): # 1 부터 100까지 반복
    co.send(i)  # 코루틴 accumulate에 숫자를 보냄
co.send(None)   # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄
"""
"""
# coroutine yield from
def number_coroutine():
    x = None
    while True:
        x = (yield x)   # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        if x == 3:
            return x

def print_coroutine():
    while True:
        x = yield from number_coroutine()   # 하위 코루틴 yield에 지정된 값을 다시 바깥으로 전달
        print('print_coroutine:', x)

co = print_coroutine()
next(co)

x = co.send(1)  # number_coroutine으로 1을 보냄
print(x)    # 1: number_coroutine의 yield에서 바깥으로 전달한 값
x = co.send(2)  # number_coroutine으로 2를 보냄
print(x)    # 2: number_coroutine의 yield에서 바깥으로 전달한 값
co.send(3)  # 3을 보내서 반환값을 출력하도록 만듦
"""
"""
# 퀴즈1
def find(word):
    result = False # True, None 도 같은 결과
    while True:
        line = (yield result)
        result = word in line

f = find('Python')
next(f)

print(f.send('Hello, Python'))
print(f.send('Hello, world'))
print(f.send('Python Script'))

f.close()
"""

# 퀴즈2
def calc():
    result = 0
    while True:
        expression = (yield result)
        a, operator, b = expression.split()
        if operator == '+':
            result = int(a) + int(b)
        elif operator == '-':
            result = int(a) - int(b)
        elif operator == '*':
            result = int(a) * int(b)
        elif operator == '/':
            result = '{:.1f}'.format(float(a) / float(b))
        else:
            result = 'Input Error'

expressions = input().split(', ')

c = calc()
next(c)

for e in expressions:
    print(c.send(e))

c.close()
