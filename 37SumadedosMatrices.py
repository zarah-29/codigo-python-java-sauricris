def sumar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    
    matriz_result = [[matriz1[i][j] + matriz2[i][j] for j in range(columnas)] for i in range(filas)]
    
    print("Matriz resultado de la suma:")
    for fila in matriz_result:
        print(fila)
    