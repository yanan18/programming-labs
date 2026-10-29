line = input("Введите целые числа через пробел: ")

numbers = []
for part in line.split():
    numbers.append(int(part))

selected = []
for number in numbers:
    if 10 <= number <= 20:
        selected.append(number)

count = len(selected)
total = sum(selected)
sorted_copy = sorted(selected)

print("Выборка:", selected)
print("Количество:", count)
print("Сумма:", total)
print("Отсортированная копия:", sorted_copy)
