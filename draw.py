"""
import turtle as t

t.shape('turtle')
for i in range(4):
    t.forward(100)
    t.right(90)
"""
"""
import turtle as t

t.shape('turtle')
for i in range(7):
    t.forward(100)
    t.right(360 / 7)
"""
"""
import turtle as t
t.shape('turtle')

n = int(input('만들고 싶은 다각형 변의 숫자를 입력하세요 :'))
for i in range(n):
    t.forward(100)
    t.right(360 / n)
"""
"""
import turtle as t

n = 6
t.shape('turtle')
t.color('pink')
t.begin_fill()
for i in range(n):
    t.forward(100)
    t.right(360 / n)
t.end_fill()
"""
"""
import turtle as t

n = 60
t.shape('turtle')
t.speed('fastest')
for i in range(n):
    t.circle(90)
    t.right(360 / n)
"""
"""
import turtle as t

t.shape('turtle')
t.speed(10)
for i in range(300):
    t.forward(i)
    t.right(91)
"""
"""
import turtle as t

n = 5
t.shape('turtle')
for i in range(n):
    t.forward(100)
    t.right((360 / n) * 2)
    t.forward(100)
    t.left(360 / n)
"""
import turtle as t

n, line = map(int, input('꼭지점 개수(5~10)와 선의 길이(50~150)을 입력 : ').split())
if 5 <= n <= 10 and 50 <= line <= 150:
    t.shape('turtle')
    t.speed('fastest')
    for i in range(n):
        t.forward(line)
        t.right((360 / n) * 2)
        t.forward(line)
        t.left(360 / n)
else:
    print('범위를 잘못 입력했습니다')
