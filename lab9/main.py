from table import row_sums, column_sums, diagonal_pattern, transform

rows = int(input("Сколько строк? "))
cols = int(input("Сколько столбцов? "))

matrix = []
for i in range(rows):
    line = input("Введите строку: ")
    parts = line.split()
    
    if len(parts) != cols:
        print("Ошибка: неверное количество чисел")
        break
    
    row = []
    for p in parts:
        row.append(int(p))
    matrix.append(row)

if len(matrix) == rows:
    print("Суммы строк:", row_sums(matrix))
    print("Суммы столбцов:", column_sums(matrix))

size = int(input("Размер узора: "))
pattern = diagonal_pattern(size)
print("Узор:")
for row in pattern:
    print(row)

print("Новая матрица:")
new_matrix = transform(matrix)
for row in new_matrix:
    print(row)
