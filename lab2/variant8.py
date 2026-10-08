total=int(input("Общее количество заданий: "))
capacity=int(input("За: "))

full=total//capacity
remainder=total%capacity
minimum=(total+capacity-1)//capacity

print("Полных комплектов:",full)
print("Остаток заданий:",remainder)
print("Всего нужно комплектов:",minimum)
