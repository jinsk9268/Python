"""
i = 0
while True:
    print(i)
    i += 1
    if i == 6:
        break
"""
"""
for i in range(100):
    print(i)
    if i == 5:
        break
"""
"""
for i in range(10):
    if i % 2 == 0 :
        continue
    print(i)
"""
"""
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
"""
"""
count = int(input('반복할 횟수를 입력하세요 : '))

i = 0
while True:
    print(i)
    i += 1
    if i == count:
        break
"""
"""
count = int(input('반복할 횟수를 입력하세요: '))

for i in range(count + 1):
    if i % 2 == 0:
        continue
    print(i)
"""
"""
i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue
    if i > 73:
        break
    print(i, end=' ')
    i += 1
"""
"""
start, stop = map(int, input().split())

i = start

while True:
    if 1>i or i>200 or 10>stop or stop>200 or i == stop or i>stop:
        print('범위를 잘못 입력했습니다')
        break
    if i % 10 == 3:
        i += 1
        continue
    if 1>i or i>200 or 10>stop or stop>200 or i == stop or i>stop or i > stop:
        break
    print(i, end=' ')
    i += 1
"""

start, stop = map(int, input().split())

i = start

if 1 > i or i > 200 or 10 > stop or stop > 200 or i == stop:
    print('잘못 입력했습니다')
else:
    while True:
        if i % 10 == 3:
            i += 1
            continue
        if i > stop:
            break
        print(i, end=' ')
        i += 1
