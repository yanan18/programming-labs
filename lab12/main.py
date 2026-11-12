import os
from storage import load_records, save_records
from logic import validate_records, add_record, find_records, set_completed, delete_record, statistics

os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILE = "data.json"

records = load_records(FILE)
try:
    validate_records(records)
except:
    print("Ошибка в файле данных!")
    records = []

while True:
    print("\n1. Показать записи")
    print("2. Добавить запись")
    print("3. Найти записи")
    print("4. Изменить статус")
    print("5. Удалить запись")
    print("6. Показать статистику")
    print("7. Сохранить данные")
    print("8. Выйти")
    
    choice = input("Выберите пункт: ")
    
    if choice == "1":
        if len(records) == 0:
            print("Нет записей.")
        else:
            sorted_recs = sorted(records, key=lambda x: x["id"])
            for r in sorted_recs:
                status = "пройден" if r["completed"] else "не пройден"
                print(f"ID: {r['id']} | {r['title']} | {r['category']} | {r['amount']} км | {status}")
                
    elif choice == "2":
        title = input("Название: ")
        if title.strip() == "":
            print("Название не может быть пустым")
            continue
        category = input("Категория: ")
        if category.strip() == "":
            print("Категория не может быть пустой")
            continue
        try:
            amount = int(input("Длина в км: "))
            if amount < 0:
                print("Длина должна быть >= 0")
                continue
        except:
            print("Введите целое число")
            continue
        add_record(records, title, category, amount)
        print("Запись добавлена!")
        
    elif choice == "3":
        q = input("Поиск по названию: ")
        found = find_records(records, q)
        if len(found) == 0:
            print("Ничего не найдено.")
        else:
            for r in found:
                print(f"ID: {r['id']} | {r['title']}")
                
    elif choice == "4":
        try:
            rid = int(input("Введите ID записи: "))
        except:
            print("Неверный ID")
            continue
        c = input("Отметить как пройденный? (да/нет): ")
        if c.lower() == "да":
            if set_completed(records, rid, True):
                print("Статус изменен!")
            else:
                print("Запись не найдена")
        elif c.lower() == "нет":
            if set_completed(records, rid, False):
                print("Статус изменен!")
            else:
                print("Запись не найдена")
                
    elif choice == "5":
        try:
            rid = int(input("Введите ID для удаления: "))
        except:
            print("Неверный ID")
            continue
        c = input("Вы уверены? (да/нет): ")
        if c.lower() == "да":
            if delete_record(records, rid):
                print("Удалено!")
            else:
                print("Запись не найдена")
                
    elif choice == "6":
        total, done, not_done, amount, cats = statistics(records)
        print(f"Всего: {total}")
        print(f"Выполнено: {done}")
        print(f"Не выполнено: {not_done}")
        print(f"Сумма км: {amount}")
        print("По категориям:")
        for cat in sorted(cats):
            print(f"  {cat}: {cats[cat]}")
            
    elif choice == "7":
        if save_records(FILE, records):
            print("Данные сохранены!")
        else:
            print("Ошибка сохранения!")
            
    elif choice == "8":
        c = input("Сохранить перед выходом? (да/нет): ")
        if c.lower() == "да":
            save_records(FILE, records)
        break
    else:
        print("Неизвестная команда")
