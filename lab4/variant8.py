n = int(input("Сколько чисел (n >= 0): "))

count = 0
total = 0

for i in range(n):
    number = int(input("Число: "))
    
    if abs(number) > 5:
        count += 1
        total += number

print("Количество:", count)
print("Сумма:", total)
