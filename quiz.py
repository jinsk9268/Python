"""
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i) == 5]
print(b)
"""

x, y = map(int, input().split())
if 1 <= x <= 20 and 10 <= y <= 30 and x < y:
    i = list(2**i for i in range(x,y+1))
    del i[1]
    del i[-2]
    print(i)
else:
    print('잘못 입력했습니다')

