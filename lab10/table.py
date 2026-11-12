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
