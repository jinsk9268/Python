"""
class Person:
    def greeting(self):
        print('Hello')

james = Person()
james.greeting()

a = int(10)
print(a)

b = list(range(10))
print(b)

c = dict(x = 10, y = 20)
print(c)

b.append(20)
print(b)

a = 10
print(type(a))

b = [0, 1, 2]
print(type(b))

c = {'x': 10, 'y': 20}
print(type(c))

maria = Person()
print(type(maria))
"""
"""
class Person:
    def greeting(self):
        print('Hello')

    def hello(self):
        self.greeting() # self.메서드() 형식으로 클래스 안의 메서드를 호출

james = Person()
james.hello()   # Hello 출력
"""
"""
class Person:
    pass

james = Person()
print(isinstance(james, Person))
"""
"""
# n이 정수가 아니거나 음수이면 함수를 끝냄
def factorial(n):
    if not isinstance(n, int) or n < 0:
        return None
    if n == 1:
        return 1
    return n * factorial(n -1)
"""
"""
# 클래스 속성
class Person:
    def __init__(self):
        self.hello = '안녕하세요.'

    def greeting(self):
        print(self.hello)

james = Person()
james.greeting()
"""
"""
# 인스턴스 만들때 값 받기
class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()

print('이름:', maria.name)
print('나이:', maria.age)
print('주소:', maria.address)
"""
"""
# 클래스 위치 인수
class Person:
    def __init__(self, *args):
        self.hello = '안녕하세요.'
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

maria = Person(*['마리아', 20, '서울시 서초구 반포동'])
maria.greeting()

print('이름:', maria.name)
print('나이:', maria.age)
print('주소:', maria.address)
"""
"""
# 클래스 키워드 인수
class Person:
    def __init__(self, **kwargs):
        self.hello = '안녕하세요.'
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

maria1 = Person(name='마리아', age=20, address='서울시 서초구 반포동')
maria2 = Person(**{'name': '마리아2', 'age': 202, 'address': '서울시 서초구 반포동2'})

maria1.greeting()
maria2.greeting()

print('이름:', maria1.name)
print('나이:', maria1.age)
print('주소:', maria1.address)

print('이름:', maria2.name)
print('나이:', maria2.age)
print('주소:', maria2.address)
"""
"""
# 인스턴스 생성 뒤 속성 추가
class Person:
    pass

maria = Person()    # 인스턴스 생성
maria.name = '마리아'  # 인스턴스를 만든 뒤 속성 추가
print(maria.name)

james = Person()
print(james.name)
"""
"""
# 인스턴스 생성 뒤 속성 추가-2
class Person:
    def greeting(self): # greeting 메서드에서 hello 속성 추가
        self.hello = '안녕하세요'

maria = Person()
#print(maria.hello)  # 아직 hello 속성이 없음

maria.greeting()    # greeting 메서드를 호출해야
print(maria.hello)  # hello 속성이 생성
"""
"""
# 특정 속성만 허용
class Person:
    __slots__ = ['name', 'age'] # name, age만 혀용(다른 속성은 생성 제한)

maria = Person()    # 인스턴스 생성
maria.name = '마리아'  # 허용된 속성
maria.age = 20  # 허용된 속성
maria.address = '서울시 서초구 반포동'   # 혀옹되지 않는 속성, 에러 발생
"""
"""
# private attribute
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet      # 비공개 속성

maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.__wallet -= 10000 # 클래스 바깥에서 비공개 속성에 접근시 에러 발생
"""
"""
# private attribute
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # 비공개 속성

    def pay(self, amount):
        self.__wallet -= amount # 비공개 속성은 클래스 안의 메서드에서만 접근 가능
        print('이제 {0}원 남았네요'.format(self.__wallet))

maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)
"""
"""
# private attribute-2
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # 비공개 속성

    def pay(self, amount):
        if amount > self.__wallet:
            print('돈이 모자라네...') # 사용금액 보다 지갑에 든 돈이 적을때
            return
        else:
            self.__wallet -= amount
            print('이제 {0}원 남았네요'.format(self.__wallet))

maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)
maria.pay(2000)
maria.pay(6000)
"""
"""
# private method
class Person:
    def __greetion(self):
        print('Hello')
    def hello(self):
        self.__greeting()   # 클래서 안에서 비공개 메서드 호출 가능

james = Person()
james.__greeting()  # 에러: 클래스 외부에서 비공개 메서드 호출 불가
"""
"""
# quiz-1
class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('베기')

x = Knight(health = 524.4, mana = 210.3, armor = 38)
print(x.health, x.mana, x.armor)
x.slash()
"""
"""
# quiz-2
class Annie:
    def __init__(self, **kwargs):
        self.health = kwargs['health']
        self.mana = kwargs['mana']
        self.ability_power = kwargs['ability_power']
    def tibbers(self):
        print('티버: 피해량', self.ability_power * 0.65 + 400)

health, mana, ability_power = map(float, input().split())

x = Annie(health = health, mana = mana, ability_power = ability_power)
x.tibbers()
"""
"""
# quiz-2
class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power
    def tibbers(self):
        AP = self.ability_power * 0.65 + 400
        print('티버: 피해량', AP)

health, mana, ability_power = map(float, input().split())

x = Annie(health = health, mana = mana, ability_power = ability_power)
x.tibbers()
"""
"""
# class class attribute
class Person:
    bag = []

    # self는 현재 인스턴스를 뜻하므로 클래스 속성을 지칭하기에는 모호
    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)
"""
"""
# class class attribute-2
class Person:
    bag = []

    # 클래스 이름으로 클래스 속성에 접근
    def put_bag(self, stuff):
        Person.bag.append(stuff)

james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(Person.bag)

print(james.__dict__)
print(Person.__dict__)
"""
"""
# 인스턴스 속성 사용하기
class Person:
    def __init__(self):
        self.bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)
"""
"""
# private class
class Knight:
    __item_limit = 10   # 비공개 클래스 속성

    def print_item_limit(self):
        print(Knight.__item_limit)  # 클래스 안에서만 접근할 수 있음

x = Knight()
x.print_item_limit()    # 10

print(Knight.__itme_limit)  # 클래스 바깥에서는 접근할 수 없음
"""
"""
# 독스트링
class Person:
    '''사람 클래스 입니다.'''

    def greeting(self):
        '''인사 메서드입니다'''
        print('Hello')

print(Person.__doc__)
print(Person.greeting.__doc__)

maria = Person()
print(maria.greeting.__doc__)
"""
"""
# static method
class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)

Calc.add(10, 20)
Calc.mul(10, 20)
"""
"""
# class method
class Person:
    count = 0   # 클래스 속성

    def __init__(self):
        Person.count += 1   # 인스턴스가 만들어질 때
                            # 클래스 속성 count에 1을 더함

    @classmethod
    def print_count(cls):
        # cls로 클래스 속성에 접근
        print('{0}명 생성되었습니다.'.format(cls.count))

james = Person()
maria = Person()

Person.print_count()
"""
"""
# 퀴즈
class Date:
    @staticmethod
    def is_date_valid(date_string):
        year, month, day = map(int, date_string.split('-'))
        return month <= 12 and day <= 31

if Date.is_date_valid('2000-13-31'):
    print('올바른 날짜 형식입니다')
else:
    print('잘못된 날짜 형식입니다.')
"""

# 퀴즈2
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return hour <= 24 and minute <= 59 and second <= 60

    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        time = cls(hour, minute, second)
        return time

time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')
