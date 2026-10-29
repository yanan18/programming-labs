line = input("Введите целые числа через пробел: ")

numbers = []
for part in line.split():
    numbers.append(int(part))

new_numbers = []
for number in numbers:
    if number < 0:
        new_numbers.append(abs(number))
    else:
        new_numbers.append(number)

print("Исходный список:", numbers)
print("Новый список:", new_numbers)
