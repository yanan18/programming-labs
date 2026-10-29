text = input("Введите текст: ")

cleaned = text.lower().replace(" ", "")

if len(cleaned) == 0:
    print("Нет текста")
else:
    is_palindrome = True
    half = len(cleaned) // 2
    
    for i in range(half):
        if cleaned[i] != cleaned[-1 - i]:
            is_palindrome = False
            break
            
    if is_palindrome:
        print("Палиндром")
    else:
        print("Не палиндром")
