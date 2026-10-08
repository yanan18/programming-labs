value=int(input("Заполнение группы(%): "))

if value<0 or value>100:
    print("Ошибка диапазона")
elif value<=39:
    print("Есть места")
elif value<=79:
    print("Группа набирается")
else:
    print("Почти заполнена")
