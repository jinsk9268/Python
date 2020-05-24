"""
# 선길이 구하기
import math

class Point2D:
    def __init__(self, x, y):   # 평면에 위치 표시
        self.x = x
        self.y = y

p1 = Point2D(x = 30, y = 20)    # 점1
p2 = Point2D(x = 60, y = 50)    # 점2

a = p2.x - p1.x     # 선 a의 길이
b = p2.y - p1.y     # 선 b의 길이

c = math.sqrt((a * a) + (b * b))    # 제곱근 구하기
# c = math.sqrt(math.pow(a, 2) + math.pow(b, 2)
# c = math.sqrt((a ** 2) + (b ** 2))
print(c)
"""
"""
# namedtuple 사용
import math
import collections

# namedtuple로 점 표현
Point2D = collections.namedtuple('Point2D', ['x', 'y'])

p1 = Point2D(x = 30, y = 20)    # 점1
p2 = Point2D(x = 60, y = 50)    # 점2

a = p1.x - p2.x     # 선 a의 길이
b = p1.y - p2.y     # 선 b의 길이

c = math.sqrt((a * a) + (b * b))
print(c)    # 42.42640687119285
"""
"""
# 퀴즈1
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

rect = Rectangle(x1 = 20, y1 = 20, x2 = 40, y2 = 30)

width = abs(rect.x2 - rect.x1)
height = abs(rect.y2 - rect.y1)
area = width * height

print(area)
"""

# quiz-2
import math

class Point2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = \
    map(int, input().split())

for i in range(len(p) - 1):
    s = math.sqrt(abs(math.pow(p[i].x - p[i+1].x, 2)) + abs(math.pow(p[i].y - p[i+1].y, 2)))
    length += s

print(length)