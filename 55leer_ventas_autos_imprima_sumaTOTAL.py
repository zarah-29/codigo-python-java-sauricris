totalven = 0
print("Ingrese las ventas. Escribe 'fin' para terminar")

while (entrada := input("Venta: ")) != "fin":
    if entrada.replace(".", "", 1).isdigit():
        totalven += float(entrada)

print(f"Total: {totalven}")