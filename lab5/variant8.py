text = input("Введите текст: ")

words = text.split()
count = 0

for word in words:
    cleaned = word.strip(".,!?:;")
    cleaned = cleaned.lower()
    
    if cleaned == "":
        continue
        
    if cleaned.count("а") == 1:
        print(cleaned)
        count += 1

if count == 0:
    print("Нет совпадений")
else:
    print("Количество:", count)
