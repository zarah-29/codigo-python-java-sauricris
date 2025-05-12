# Crear una matriz de 3x3
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Leer valores enteros para la matriz
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Ingrese valor entero para la posición ({i+1}, {j+1}): "))

# Imprimir la matriz
print("Matriz:")
for fila in matriz:
    print(fila)