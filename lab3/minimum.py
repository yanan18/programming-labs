a=int(input("Первое число: "))
b=int(input("Второе число: "))
c=int(input("Третье число: "))

if a<=b and a<=c:
    print("Минимум:",a)
elif b <= a and b <=c:
    print("Минимум:",b)
else:
    print("Минимум:",c)
