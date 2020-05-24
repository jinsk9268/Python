"""
for i in range(1,6):
    print('*'*i)

print()

for i in range(1,6):
    print('*'*(6-i))

print()

for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end='')
        else :
            print(' ', end='')
    print()

print()

for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')
    print()

print()

for i in range(5):
    for j in range(5):
        if j >= i:
            print('*', end='')
    print()

print()

for i in range(5):
    for j in range(5):
        print('*', end='')
    print()

print()
"""

x = int(input())

for i in range(x): 
    for j in range(x): 
        if j < (x-1-i):
            print(' ', end='')
        else:
            print('*', end='')
    print('*'*i, end='')
    print()

"""
x = int(input())

for i in range(x):
    for j in reversed(range(x)):
        if j > i:
            print(' ', end='')
        else:
            print('*', end='')
    for j in range(x):
        if j < i:
            print('*', end='')
    print()
"""
"""
x = int(input())

for i in range(x):
    for j in reversed(range(x)):
        if j > i:
            print(' ', end='')
        else:
            print('*', end='')
            
    print('*'*i, end='')
    print()
"""
