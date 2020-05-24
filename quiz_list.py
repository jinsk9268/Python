"""
for i in range(row):
    line = []
    for j in range(col):
        line.append(input())
    matrix.append(line)
"""
"""
for i in range(row):
    add = list(input())
    if len(add) == 3:
        matrix.append(list(input()))
    else:
        print('잘못 입력했습니다')
"""
row, col = map(int, input().split())
matrix = []

count = 0
while count < row:
    add = list(input())
    if len(add) == col:
        matrix.append(add)
        count += 1
    else:
        print('개수를 잘못 입력했습니다')
new_matrix = []
for i in range(len(matrix)):
    line = []
    for j in range(len(matrix[i])):
        add_val = 0
        if matrix[i][j] == '*':
            line.append(matrix[i][j])
        else:
            for add_row in range(-1, 2):
                for add_col in range(-1, 2):
                    if i + add_row < 0 or j + add_col < 0 or i + add_row >= row or j + add_col >= col:
                        # add_val += 0
                        continue
                    elif matrix[i + add_row][j + add_col] == '*':
                        add_val += 1
                    elif matrix[i + add_row][j + add_col] == matrix[i][j]:
                        # add_val += 0
                        continue
                    else:
                        # add_val += 0
                        continue
            line.append(add_val)
    new_matrix.append(line)

for a in range(len(new_matrix)):
    for b in range(len(new_matrix[a])):
        print(new_matrix[a][b], end = ' ')
    print()
