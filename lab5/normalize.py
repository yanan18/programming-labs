text = input("Введите текст: ")

normalized = " ".join(text.split())

print("Исходная длина:", len(text))
print("Новая длина:", len(normalized))
print("Текст:", normalized)
print("Количество слов:", len(normalized.split()))
