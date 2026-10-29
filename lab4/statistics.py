n = int(input("Сколько чисел (n >= 1): "))

total = 0
positive_count = 0

for i in range(n):
    number = int(input("Число: "))
    
    total += number
    
    if number > 0:
        positive_count += 1
        
    if i == 0:
        maximum = number
    else:
        if number > maximum:
            maximum = number

print("Сумма:", total)
print("Положительных:", positive_count)
print("Максимум:", maximum)
