text = input("Введите текст: ")

cleaned = text.lower().replace(" ", "")

if len(cleaned) == 0:
    print("Нет текста")
else:
    if cleaned == cleaned[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")
