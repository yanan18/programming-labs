line = input("Введите целые числа через пробел: ")

if line == "":
    print("Нет данных")
else:
    numbers = []
    for part in line.split():
        numbers.append(int(part))
        
    maximum = max(numbers)
    result = []
    
    for index, value in enumerate(numbers):
        if value == maximum:
            result.append(index)
            
    print(result)
