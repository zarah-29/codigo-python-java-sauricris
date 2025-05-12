def sumar_vectores(vector1, vector2):
    # Verificar si los vectores tienen la misma longitud
    if len(vector1) != len(vector2):
        raise ValueError("Los vectores deben tener la misma longitud")

    # Sumar los vectores
    vector_resultado = [a + b for a, b in zip(vector1, vector2)]

    return vector_resultado