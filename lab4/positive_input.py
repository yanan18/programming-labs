attempts = 0

while True:
    number = int(input("Введите положительное число: "))
    
    if number > 0:
        print("Квадрат:", number ** 2)
        print("Отклонено попыток:", attempts)
        break
    else:
        attempts += 1
