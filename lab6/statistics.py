line = input("Введите целые числа через пробел: ")

if line == "":
    print("Нет данных")
else:
    numbers = []
    for part in line.split():
        numbers.append(int(part))
    
    count = len(numbers)
    total = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    average = total / count
    
    print("Количество:", count)
    print("Сумма:", total)
    print("Минимум:", minimum)
    print("Максимум:", maximum)
    print(f"Среднее: {average:.2f}")
