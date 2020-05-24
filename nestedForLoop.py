"""
a = [[10, 20], [30, 40], [50, 60]]
for i in a:
    for j in i:
        print(j, end = ' ')
    print()
"""
"""
a = [[10, 20], [30, 40], [50, 60]]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()
"""
"""
a = [[10, 20], [30, 40], [50, 60]]

i = 0
while i < len(a):
    x, y = a[i]
    print(x, y)
    i += 1
"""
"""
a = [[10, 20], [30, 40], [50, 60]]

i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end = ' ')
        j += 1
    print()
    i += 1
"""
"""
a = []

for i in range(10):
    a.append(0)

print(a)
"""
"""
a = []

for i in range(3):
    line = []
    for j in range(2):
        line.append(0)
    a.append(line)

print(a)
"""
"""
a = [[0 for j in range(2)] for i in range(3)]
print(a)
"""
"""
a = [[0] * 2 for i in range(3)]
print(a)
"""
"""
a = [3, 1, 3, 2, 5]
b = []

for i in a:
    line = []
    for j in range(i):
        line.append(0)
    b.append(line)

print(b)
"""
"""
a = [[0] * i for i in [3, 1, 3, 2, 5]]
print(a)
"""

std = [
    ['john', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 7]
      ]

print(sorted(std, key = lambda std: std[0]))
print(sorted(std, key = lambda std: std[1]))
print(sorted(std, key = lambda std: std[2]))

print(sorted(std, key = lambda std: std[0], reverse = True))
print(sorted(std, key = lambda std: std[1], reverse = True))
print(sorted(std, key = lambda std: std[2], reverse = True))
