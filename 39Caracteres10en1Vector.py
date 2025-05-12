def leer_caracteres():
    vector = []
    for i in range(10):
        caracter = input(f"Ingrese caracter {i+1}: ")
        vector.append(caracter)
    return vector

vector = leer_caracteres()
print("Vector de caracteres:")
print(vector)