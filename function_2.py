"""
def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)


print_numbers(10, 20, 30)

x = [10, 20, 30]
print_numbers(*x)

# 에러
print_numbers(*[10, 20])
"""
"""
def print_numbers(*args):
    for arg in args:
        print(arg)


print_numbers(10)
print('\n')
print_numbers(10, 20, 30, 40)
print('\n')

x = [10]
print_numbers(*x)
print('\n')
y = [10, 20, 30, 40]
print_numbers(*y)
"""
"""
# 매개변수 순서에서 *args는 반드시 가장 뒤쪽에 와야한다
def print_numbers(a, *args):
    print(a)
    print(args)

print_numbers(1)

print_numbers(1, 10, 20)

print_numbers(*[10, 20, 30])
"""
"""
def personal_info(name, age, address):
    print('이름 : ', name)
    print('나이 : ', age)
    print('주소 : ', address)


personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')

# 키워드 인수를 사용하면 순서를 지키지 않아도 순서대로 출력
personal_info(age = 30, address = '서울시 용산구 이촌동', name = '홍길동')
"""
"""
def personal_info(name, age, address):
    print('이름 : ', name)
    print('나이 : ', age)
    print('주소 : ', address)

x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}

personal_info(**x)

# 딕셔너리 앞에 바로 \**을 붙여도 동작은 같다
personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})

# 매개변수 이름, 개수 딕셔너리 키이름, 개수 가 다를때
#personal_info(**{'name': '홍길동', 'old': 30, 'address': '서울시 용산구 이촌동'})
#personal_info(**{'name': '홍길동', 'age': 30})

personal_info(*x)
"""

def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')
"""
# 인수를 직접 넣기
personal_info(name='홍길동')

personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')

# 딕셔너리 언패킹 사용
x = {'name': '홍길동'}
y = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}

personal_info(**x)

personal_info(**y)
"""
"""
def personal_info(**kwargs):
    if 'name' in kwargs:
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])

x = {'name': '홍길동'}
y = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}

personal_info(**x)

personal_info(**y)
"""
"""
def personal_info(name, **kwargs):
    print(name)
    print(kwargs)

personal_info('홍길동')

personal_info('홍길동', age=30, address='서울시 용산구 이촌동')

personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})
"""
"""
def custom_print(*args, **kwargs):
    print(*args, **kwargs)

custom_print(1, 2, 3, sep=':', end='')
"""
"""
def personal_info(name, age, address='비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info('홍길동', 30)

# parameter에 초깃값이 있더라도 값을 넣으면 해당 값이 전달
personal_info('홍길동', 30, '서울시 용산구 이촌동')
"""
"""
# 초깃값 지정된 parameter 위치 잘못 되어있음, 에러 발생
def personal_info(name, address='비공개', age):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info('홍길동', 30)
"""
"""
# 퀴즈1
korean, english, mathematics, science = 100, 86, 81, 91

def get_max_score(*args):
    return max(args)

max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수: ', max_score)

max_score = get_max_score(english, science)
print('높은 점수: ', max_score)
"""

# 퀴즈2
korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):
    return min(args), max(args)

def get_average(**kwargs):
    return float(sum(kwargs.values()) / len(kwargs))

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english, mathematics=mathematics, science=science)

print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균점수: {2:.2f}'.format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)

print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))