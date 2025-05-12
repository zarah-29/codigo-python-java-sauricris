def leer_caracteres():
    s = int(input("Ingrese el tamaño del vector: "))
    vector = []
    for i in range(s):
        caracter = input(f"Introduce el caracter {i + 1}: ")
        vector.append(caracter)
    print("El vector resultante es:")
    for i in range(s):
        print(vector[i])

leer_caracteres()