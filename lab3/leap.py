year=int(input("Год: "))

if year%400==0 or (year%4==0 and year%100!=0):
    print("Да")
else:
    print("Нет")
