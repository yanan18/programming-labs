def sum_digits(number):
    """Возвращает сумму цифр модуля числа."""
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number = number // 10
    return total


def average(numbers):
    """Возвращает среднее арифметическое или None для пустого списка."""
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    """Возвращает строку в нижнем регистре без лишних пробелов."""
    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):
    """Возвращает числа, модуль которых не больше порога (вариант 8)."""
    result = []
    for number in numbers:
        if abs(number) <= threshold:
            result.append(number)
    return result
