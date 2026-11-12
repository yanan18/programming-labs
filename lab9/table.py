def row_sums(matrix):
    sums = []
    for row in matrix:
        s = 0
        for number in row:
            s = s + number
        sums.append(s)
    return sums


def column_sums(matrix):
    if len(matrix) == 0:
        return []
    
    sums = []
    for j in range(len(matrix[0])):
        s = 0
        for i in range(len(matrix)):
            s = s + matrix[i][j]
        sums.append(s)
    return sums


def diagonal_pattern(size):
    result = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(0)
            elif i < j:
                row.append(1)
            else:
                row.append(2)
        result.append(row)
    return result


def transform(matrix):
    new_matrix = []
    for row in matrix:
        new_row = []
        for number in row:
            if number < 0:
                new_row.append(number - 2)
            else:
                new_row.append(number)
        new_matrix.append(new_row)
    return new_matrix
