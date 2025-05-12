Me = [[0 for _ in range(5)] for _ in range(5)]

for i in range(1, 6):
    for j in range(1, 6):
        Me[i-1][j-1] = 0

for fila in Me:
    print(fila)