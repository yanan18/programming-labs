from files_lab import read_matrix, selected_sum
from table import row_sums, column_sums

def read_positive_integer():
    while True:
        text = input("Введите целое число больше нуля: ")
        try:
            number = int(text)
            if number <= 0:
                print("Должно быть больше нуля")
            else:
                return number
        except ValueError:
            print("Не целое число")

read_positive_integer()
print("Ввод размера пройден!")

try:
    matrix = read_matrix("matrix.txt")
    print("Матрица прочитана:", matrix)
    
    r_sums = row_sums(matrix)
    c_sums = column_sums(matrix)
    v_sum = selected_sum(matrix)
    
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(f"Суммы строк: {r_sums}\n")
        f.write(f"Суммы столбцов: {c_sums}\n")
        f.write(f"Результат варианта: {v_sum}\n")
        
    print("Отчет записан!")
    
except Exception as e:
    print("Ошибка:", e)
