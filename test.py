"""
import string
x = input().split()
count = 0
for i in x:
    if i.strip(string.punctuation) == 'the':
        count += 1
    else:
        continue

print(count)
"""
"""
x = input().split(';')
b = []
for i in x:
    b.append(int(i))
b.sort(reverse = True)
for i in b:
    print('{:>9,}'.format(i))
"""
x = map(int, input().split(';'))
y = list(x)
y.sort(reverse = True)
for i in y:
    print('{:>9,}'.format(i))



