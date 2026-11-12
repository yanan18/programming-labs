from files_lab import read_matrix, selected_sum

with open("test.txt", "w", encoding="utf-8") as f:
    f.write("1 2\n7 -1\n")

m = read_matrix("test.txt")
assert m == [[7, -1]]

try:
    with open("bad.txt", "w", encoding="utf-8") as f:
        f.write("")
    read_matrix("bad.txt")
    assert False, "Ошибка не обнаружена"
except ValueError:
    pass

assert selected_sum([[1, -2, 3], [4, 0, -6]]) == 2

print("Все проверки пройдены!")
