"""
for i in range(1, 101): # 1~100까지 100번 반복
    print(i)
"""
"""
for i in range(1, 101):
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
"""
"""
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
"""
"""
for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
"""
"""
for i in range(1, 101):
    print('Fizz' * (i % 3 ==0) + 'Buzz' * (i % 5 == 0) or i)
"""
"""
for i in range(1, 101):
    if i % 2 == 0 and i % 11 == 0:
        print('FizzBuzz')
    elif i % 2 == 0:
        print('Fizz')
    elif i % 11 == 0:
        print('Buzz')
    else:
        print(i)
"""

x, y = map(int, input().split())
if 1 <= x <= 1000 and 10 <= y < 1000 and x < y:
    for i in range(x, y+1):
        if i % 5 == 0 and i % 7 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Fizz')
        elif i % 7 == 0:
            print('Buzz')
        else:
            print(i)
else:
    print('범위를 잘못 입력했습니다')
    
