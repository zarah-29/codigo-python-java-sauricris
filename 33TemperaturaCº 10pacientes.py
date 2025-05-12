temperaturas = []
for i in range(10):
    temperatura = float(input(f"Temperatura {i+1}: "))
    temperaturas.append(temperatura)

print("Las temperaturas de los 10 pacientes en Celsius son:")
for temperatura in temperaturas:
    print(temperatura)