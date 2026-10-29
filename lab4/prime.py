n = int(input("Введите целое число (n >= 2): "))

is_prime = True
divisor = 2

while divisor * divisor <= n:
    if n % divisor == 0:
        is_prime = False
        break
    divisor += 1

if is_prime:
    print("Простое")
else:
    print("Не простое")
