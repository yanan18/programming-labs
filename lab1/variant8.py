order=input("Заказ: ")
customer=input("Заказчик: ")

name1=input("Первая позиция: ")
qty1=int(input("Количество: "))
price1=float(input("Цена: "))

name2=input("Вторая позиция: ")
qty2=int(input("Количество: "))
price2=float(input("Цена: "))

delivery=float(input("Доставка: "))
paid=float(input("Внесено: "))
discount=float(input("Скидка в %: "))

cost1=qty1*price1
cost2=qty2*price2
goods=cost1+cost2
disc=goods*discount/100
goods_after=goods-disc
total=goods_after+delivery
change=paid-total

print()
print("Заказ:",order)
print("Заказчик:",customer)
print(name1, "|",qty1,"|",price1,"|",cost1)
print(name2, "|",qty2,"|",price2,"|",cost2)
print("Товары:",goods)
print("Скидка:",disc)
print("Товары со скидкой:",goods_after)
print("Доставка:",delivery)
print("Итого:",total)
print("Количество:",qty1+qty2)
print("Сдача:",change)
