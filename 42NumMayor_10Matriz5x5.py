matriz = [
    [1, 12, 3, 16, 5],
    [6, 7, 8, 9, 10],
    [11, 2, 13, 14, 3],
    [4, 15, 1, 17, 18],
    [19, 20, 2, 21, 22]
]
contador_mayores_10 = 0
for fila in matriz:
    for elemento in fila:
       if elemento > 10:
            contador_mayores_10 += 1
print("Número de elementos mayores a 10:", contador_mayores_10)