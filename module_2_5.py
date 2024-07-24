def get_matrix(n, m, value):
    matrix = []
    line = []
    for i in range(0, n):
        line.append(value)
    for j in range(0, m):
        matrix.append(line)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)