from functions import sum_digits, average, normalize_text, select_numbers

number = int(input("Введите целое число: "))
print("Сумма цифр:", sum_digits(number))

line = input("Введите числа через пробел: ")
numbers = []
for part in line.split():
    numbers.append(int(part))

avg = average(numbers)
if avg is None:
    print("Нет данных")
else:
    print(f"Среднее: {avg:.2f}")

text = input("Введите текст: ")
print("Нормализованный текст:", normalize_text(text))

threshold = int(input("Введите порог: "))
selected = select_numbers(numbers, threshold)
print("Подходящие числа:", selected)
