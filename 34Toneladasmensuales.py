toneladas = []
for i in range(12):
    toneladas.append(float(input(f"Ingrese toneladas {i + 1} de 2024: ")))

print(f"Toneladas mensuales de 2024: {toneladas}")
promedio = sum(toneladas) / len(toneladas)
print(f"Promedio de toneladas de 2024: {promedio}")
    

