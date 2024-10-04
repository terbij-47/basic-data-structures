def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row) # либо matrix.append([value] * m) вместо цикла
    return matrix

print(get_matrix(4, 2, 13))
