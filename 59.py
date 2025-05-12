V1 = [int(input(f"Ingrese el número {i + 1} para el primer vector: ")) for i in range(10)]
V2 = [int(input(f"Ingrese el número {i + 1} para el segundo vector: ")) for i in range(10)]

for i in range(10):
    suma = V1[i] + V2[i]
    print(f"{V1[i]} + {V2[i]} = {suma}")