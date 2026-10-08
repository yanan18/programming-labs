sub1=input("Первый предмет: ")
n1=int(input("Занятий в неделю: "))
m1=int(input("Минут на занятие: "))

sub2=input("Второй предмет: ")
n2=int(input("Занятий в неделю: "))
m2=int(input("Минут на занятие: "))

free=float(input("Доступно часов в неделю: "))

total1=n1*m1
total2=n2*m2
total=total1+total2

print()
print(sub1,":",total1,"минут")
print(sub2,":",total2,"минут")
print("Всего:",total,"минут или",total/60,"часов")
print("Остаток:",free-total/60,"часов")
print("За 4 недели:",total/60*4,"часов")
