price=int(input("Цена одной тетради (руб.): "))
count=int(input("Количество тетрадей: "))
paid=int(input("Переданная сумма (руб.): "))

cost=price*count
change=paid-cost

print("Стоимость:",cost,"сдача:",change)
