from collections_lab import (word_counts, common_topics, all_topics, 
                             totals_by_category, titles_in_category)

# Проверки word_counts
assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
assert word_counts("!!!") == {}
assert word_counts("") == {}

# Проверки тем
assert common_topics(["python", "sql", "python"], ["sql", "git"]) == ["sql"]
assert all_topics(["python", "sql", "python"], ["sql", "git"]) == ["git", "python", "sql"]
assert common_topics([], ["sql"]) == []
assert all_topics([], ["sql"]) == ["sql"]

# Проверки варианта (суммы и названия)
records = [
    {"title": "А", "category": "основное", "amount": 4},
    {"title": "В", "category": "дополнительное", "amount": 2},
    {"title": "С", "category": "основное", "amount": 3},
]

assert totals_by_category(records) == {"основное": 7, "дополнительное": 2}
assert totals_by_category([]) == {}

assert titles_in_category(records, "основное") == ["А", "С"]
assert titles_in_category(records, "нет") == []

# Проверка на сохранение исходных записей
records_copy = [record.copy() for record in records]
totals_by_category(records)
assert records == records_copy

print("Все проверки пройдены!")
