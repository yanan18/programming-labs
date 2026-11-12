def read_matrix(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    if len(lines) == 0:
        raise ValueError("Файл пустой")
        
    header = lines[0].split()
    rows = int(header[0])
    cols = int(header[1])

    matrix = []
    for i in range(1, rows + 1):
        parts = lines[i].split()
        if len(parts) != cols:
            raise ValueError(f"В строке {i+1} должно быть {cols} чисел")
            
        row = []
        for p in parts:
            row.append(int(p))
        matrix.append(row)
        
    return matrix


def selected_sum(matrix):
    if len(matrix) == 0:
        return 0
    total = 0
    for number in matrix[0]:
        total = total + number
    return total
