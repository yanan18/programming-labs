def word_counts(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        cleaned = word.strip(".,!?:;")
        if cleaned != "":
            counts[cleaned] = counts.get(cleaned, 0) + 1
    return counts


def print_counts(counts):
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    set1 = set(first)
    set2 = set(second)
    return sorted(set1 & set2)


def all_topics(first, second):
    set1 = set(first)
    set2 = set(second)
    return sorted(set1 | set2)


def totals_by_category(records):
    totals = {}
    for record in records:
        cat = record["category"]
        amount = record["amount"]
        totals[cat] = totals.get(cat, 0) + amount
    return totals


def titles_in_category(records, category):
    result = []
    for record in records:
        if record["category"] == category:
            result.append(record["title"])
    return result


def record_and_tuple():
    record = {"title": "Python", "hours": 40}
    record["hours"] = 50
    record["completed"] = False
    
    pair = (record["title"], record["hours"])
    title, hours = pair
    
    print("Запись:", record)
    print("Пара:", pair)
    print("Распаковано:", title, hours)


if __name__ == "__main__":
    print("Частоты слов:")
    print_counts(word_counts("Python, python! SQL"))
    
    print("\nОбщие темы:", common_topics(["python", "sql", "python"], ["sql", "git"]))
    print("Все темы:", all_topics(["python", "sql", "python"], ["sql", "git"]))
    
    records = [
        {"title": "Маршрут 1", "category": "горы", "amount": 15},
        {"title": "Маршрут 2", "category": "море", "amount": 10},
        {"title": "Маршрут 3", "category": "горы", "amount": 5}
    ]
    print("\nСуммы по категориям:", totals_by_category(records))
    print("Названия в категории 'горы':", titles_in_category(records, "горы"))
    
    print("\nЗапись и кортеж:")
    record_and_tuple()
