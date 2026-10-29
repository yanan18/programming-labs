line = input("Введите целые числа через пробел: ")

numbers = []
for part in line.split():
    numbers.append(int(part))

result = []
for number in numbers:
    if number not in result:
        result.append(number)

print("Без повторов:", result)
