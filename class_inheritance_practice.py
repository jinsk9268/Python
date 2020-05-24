"""
# inheritance
class Person:
    def greeting(self):
        print('안녕하세요')

class Student(Person):  # Person 클래스 상속
    def study(self):
        print('공부하기')

james = Student()   # Student 인스턴스 생성
james.greeting()    # 부모 클래스 Person의 메서드 호출
james.study()       # 자식 클래스 Student의 메서드 호출

print(issubclass(Student, Person))
"""
"""
# has-a관계
class Person:
    def greeting(self):
        print('안녕하세요')

class PersonList:
    def __init__(self):
        self.person_list = []   # 리스트 속성에 Person 인스턴스를 넣어서 관리

    def append_person(self, person):    # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person)
"""
"""
# super
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()  # super()로 기반 클래스의  __init__ 호출
        self.school = '파이썬 코딩 도장'

james = Student()
print(james.school)
print(james.hello)
"""
"""
# super-2
class Person:
    def __init__(self):
        print('Person__init__')
        self.hello = '안녕하세요'

class Student(Person):
    pass

james = Student()
print(james.hello)
"""
"""
# super-3
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super(Student, self).__init__()  # super()로 기반 클래스의  __init__ 호출
        self.school = '파이썬 코딩 도장'

james = Student()
print(james.school)
print(james.hello)
"""
"""
# overriding
class Person:
    def greeting(self):
        print('안녕하세요')

class Student(Person):
    def greeting(self):
        super().greeting()
        print('저는 파이썬 코딩도장 학생입니다')

james = Student()
james.greeting()
"""
"""
# multiple ingeritance
class Person:
    def greeting(self):
        print('안녕하세요')

class University:
    def manage_credit(self):
        print('학점 관리')

class Undergraduate(Person, University):
    def study(self):
        print('공부하기')

james = Undergraduate()
james.greeting()    # 기반 클래스 Person 메서드 호출
james.manage_credit()   # 기반 클래스 University 메서드 호출
james.study()   # 파생 클래스 Undergraduate 메서드 호출
"""
"""
# diamond inheritance
class A:
    def greeting(self):
        print('안녕하세요. A입니다.')
class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')

class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')

class D(B, C):
    pass

x = D()
x.greeting()
print(D.mro())
"""
"""
# abstract class
from abc import *

class StudentBase(metaclass = ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기')
        
    # 에러 발생 go_to_school 메서드도 구현
    
james = Student()
james.study()
"""
"""
# abstract class-2
from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass


class Student(StudentBase):
    def study(self):
        print('공부하기')

    def go_to_school(self):
        print('학교가기')

james = Student()
james.study()
james.go_to_school()
"""
"""
# 퀴즈-1
class AdvancedList(list):
    def replace(self, old, new):
        while old in self:
            self[self.index(old)] = new

x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)
"""

# quiz-2
class Animal:
    def eat(self):
        print('먹다')

class Wing:
    def flap(self):
        print('파닥거리다')

class Bird(Animal, Wing):
    def fly(self):
        print('날다')

b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Animal))