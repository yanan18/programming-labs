from table import row_sums, column_sums, diagonal_pattern, transform

m1 = [[1, 2, 3], [4, 5, 6]]
assert row_sums(m1) == [6, 15]
assert column_sums(m1) == [5, 7, 9]

assert row_sums([]) == []
assert column_sums([]) == []

assert diagonal_pattern(1) == [[0]]
assert diagonal_pattern(3) == [[0, 1, 1], [2, 0, 1], [2, 2, 0]]

m2 = [[-2, 0, 3], [4, -5, 6]]
expected = [[-4, 0, 3], [4, -7, 6]]
res = transform(m2)

assert res == expected
res[0][0] = 100
assert m2[0][0] == -2

print("Все проверки пройдены!")
