from functions import sum_digits, average, normalize_text, select_numbers

# Базовые проверки из задания
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир ") == "привет мир"
assert normalize_text("   ") == ""

print("Базовые проверки пройдены")

# Проверки моего варианта (8: модуль не больше порога)
numbers = [-5, 0, 2, 5]
assert select_numbers(numbers, 2) == [0, 2]
assert select_numbers([], 2) == []
assert select_numbers([3, -3, 5, -5], 3) == [3, -3]

# Проверка на сохранение исходного списка
original = [-5, 0, 2, 5]
copy = original.copy()
select_numbers(original, 2)
assert original == copy

print("Проверки варианта пройдены")
